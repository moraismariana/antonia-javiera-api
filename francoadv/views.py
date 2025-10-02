from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

import smtplib
import ssl
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

from francoadv.models import PaginaInicio, PaginaSobre, PaginaServicos, ComponenteInsta, ComponenteContato, ComponenteCTA, Servico, Artigo

from francoadv.serializers import PaginaInicioSerializer, PaginaSobreSerializer, PaginaServicosSerializer, ComponenteInstaSerializer, ComponenteContatoSerializer, ComponenteCTASerializer, ServicoSerializer, FormularioContatoSerializer, ArtigoSerializer

# Permissões
class PermissaoFrancoadv(permissions.BasePermission):
    """
    Permissão personalizada para permitir leitura para qualquer um,
    mas escrita apenas para usuários do grupo 'Admin FrancoAdv'.
    """
    message = "Você não tem permissão para realizar esta ação."

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.groups.filter(name='Admin FrancoAdv').exists()

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        groups = [group.name for group in user.groups.all()]
        return Response({
            'username': user.username,
            'groups': groups,
        })
    
class ArtigoViewSet(viewsets.ModelViewSet):
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10
    permission_classes = [IsAuthenticatedOrReadOnly, PermissaoFrancoadv]

    def get_queryset(self):
        queryset = Artigo.objects.all()
        query = self.request.query_params.get('q')
        if query:
            queryset = queryset.filter(
                Q(titulo__icontains=query) | Q(descricao__icontains=query)
            )

        # Aplica a lógica de ordenação:
        queryset = queryset.order_by('-fixado', '-data_criacao')

        return queryset

# CMS
class PaginaInicioViewSet(viewsets.ModelViewSet):
    queryset = PaginaInicio.objects.all()
    serializer_class = PaginaInicioSerializer
    permission_classes = [PermissaoFrancoadv]

class PaginaSobreViewSet(viewsets.ModelViewSet):
    queryset = PaginaSobre.objects.all()
    serializer_class = PaginaSobreSerializer
    permission_classes = [PermissaoFrancoadv]

class PaginaServicosViewSet(viewsets.ModelViewSet):
    queryset = PaginaServicos.objects.all()
    serializer_class = PaginaServicosSerializer
    permission_classes = [PermissaoFrancoadv]

class ComponenteInstaViewSet(viewsets.ModelViewSet):
    queryset = ComponenteInsta.objects.all()
    serializer_class = ComponenteInstaSerializer
    permission_classes = [PermissaoFrancoadv]

class ComponenteContatoViewSet(viewsets.ModelViewSet):
    queryset = ComponenteContato.objects.all()
    serializer_class = ComponenteContatoSerializer
    permission_classes = [PermissaoFrancoadv]

class ComponenteCTAViewSet(viewsets.ModelViewSet):
    queryset = ComponenteCTA.objects.all()
    serializer_class = ComponenteCTASerializer
    permission_classes = [PermissaoFrancoadv]

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    ordering = ['id']
    permission_classes = [PermissaoFrancoadv]

# Formulário contato
class FormularioContatoViewSet(viewsets.ViewSet):
    serializer_class = FormularioContatoSerializer
    permission_classes = [PermissaoFrancoadv]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            nome_remetente_form = serializer.validated_data['nome']
            email_remetente_form = serializer.validated_data['email']
            telefone_remetente_form = serializer.validated_data['telefone']
            mensagem_form = serializer.validated_data['mensagem']

            # --- Configurações do Zoho Mail (direto na ViewSet, como solicitado) ---
            ZOHO_SMTP_SERVER = "smtp.zoho.com"  # Ou smtppro.zoho.com para planos pagos/outras regiões
            ZOHO_SMTP_PORT = 465  # Para SSL
            # ZOHO_SMTP_PORT = 587 # Para TLS/STARTTLS (requer server.starttls() após conexão)

            # ATENÇÃO: Substitua com suas credenciais reais!
            ZOHO_EMAIL_SENDER = "no-reply@advocaciafranco.adv.br"
            ZOHO_EMAIL_PASSWORD = "No-reply1"
            NOME_REMETENTE_EMAIL = "Contato Site" # Nome que aparecerá no "De:"

            EMAIL_DESTINO = "clarissa@advocaciafranco.adv.br"

            assunto = "Advocacia Franco: Nova mensagem recebida através do site"

            corpo_email_texto = f"""
Olá! Um novo email foi recebido através do seu site:

Nome: {nome_remetente_form}
Email: {email_remetente_form}
Telefone: {telefone_remetente_form}

Mensagem: {mensagem_form}

Importante: Não responda diretamente através deste email, e sim inicie uma nova conversa endereçada ao destinatário.
            """

            # Criando o objeto do email
            msg = MIMEText(corpo_email_texto, 'plain', 'utf-8')
            msg['Subject'] = Header(assunto, 'utf-8')
            # formataddr lida bem com nomes que podem ter caracteres especiais
            msg['From'] = formataddr((str(Header(NOME_REMETENTE_EMAIL, 'utf-8')), ZOHO_EMAIL_SENDER))
            msg['To'] = EMAIL_DESTINO

            try:
                # Criar contexto SSL seguro
                context = ssl.create_default_context()

                # Usando SMTP_SSL para conexão SSL direta na porta 465
                with smtplib.SMTP_SSL(ZOHO_SMTP_SERVER, ZOHO_SMTP_PORT, context=context) as server:
                    server.login(ZOHO_EMAIL_SENDER, ZOHO_EMAIL_PASSWORD)
                    server.sendmail(ZOHO_EMAIL_SENDER, [EMAIL_DESTINO], msg.as_string())
                
                return Response({'mensagem': 'Email enviado com sucesso!'}, status=status.HTTP_200_OK)

            except smtplib.SMTPAuthenticationError:
                # Erro comum: credenciais inválidas ou necessidade de senha de aplicativo
                print(f"Erro de autenticação SMTP com Zoho. Verifique email/senha e se 2FA requer senha de app.")
                # Não exponha detalhes demais ao cliente
                return Response(
                    {'mensagem': 'Erro ao autenticar com o servidor de email.'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            except smtplib.SMTPServerDisconnected:
                print("Servidor SMTP desconectou inesperadamente.")
                return Response(
                    {'mensagem': 'O servidor de email desconectou. Tente novamente mais tarde.'},
                    status=status.HTTP_503_SERVICE_UNAVAILABLE
                )
            except smtplib.SMTPException as e:
                # Captura outras exceções SMTP
                print(f"Erro SMTP ao enviar email: {e}")
                return Response(
                    {'mensagem': 'Ocorreu um erro ao tentar enviar o email.', 'erro_tecnico': str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            except Exception as e:
                # Captura qualquer outra exceção
                print(f"Erro inesperado ao enviar email: {e}")
                return Response(
                    {'mensagem': 'Ocorreu um erro inesperado no servidor.', 'erro_tecnico': str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            # Retorna os erros de validação para o frontend
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)