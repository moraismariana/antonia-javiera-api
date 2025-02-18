from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, From

from javiera.models import Artigo, InicioTexto, InicioImg, InicioBg, SobreTexto, SobreImg, ComponenteArtigosTexto, ComponenteContatoTexto, PaginaInicio, ComponenteContato

from javiera.serializers import ArtigoSerializer, FormularioContatoSerializer, InicioTextoSerializer, InicioImgSerializer, InicioBgSerializer, SobreTextoSerializer, SobreImgSerializer, ComponenteArtigosTextoSerializer, ComponenteContatoTextoSerializer, PaginaInicioSerializer, ComponenteContatoSerializer

# Views para os modelos

class ArtigoViewSet(viewsets.ModelViewSet):
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 8

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

# View para Formulário de Contato (enviar email com sendgrid)

load_dotenv()

class FormularioContatoViewSet(viewsets.ViewSet):
    serializer_class = FormularioContatoSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data['nome']
            email_remetente = serializer.validated_data['email']
            mensagem = serializer.validated_data['mensagem']

            assunto = f"Novo email recebido pelo site"
            mensagem_email = f'<p>Olá, Antonia! Um novo email foi recebido através do seu site:</p><br><p><strong>Nome:</strong> {nome}</p><p><strong>Email:</strong> {email_remetente}</p><p><strong>Mensagem:</strong> {mensagem}</p><br><p>Importante: Não responda diretamente através deste email, e sim inicie uma nova conversa endereçada ao destinatário.</p>'
            email_destino = ['moraismariana200@gmail.com']

            email_sendgrid = Mail(
                from_email = From('no-reply@moraismariana.com', 'Site Antonia Javiera'),
                to_emails = email_destino,
                subject = assunto,
                html_content = mensagem_email
            )

            try:
                api_key = os.environ.get('SENDGRID_API_KEY')
                print(f"API Key lida do ambiente: {api_key}")
                sg = SendGridAPIClient(api_key)
                response = sg.send(email_sendgrid)
                if response.status_code == 202:
                    return Response({'mensagem': 'Email enviado com sucesso!'}, status = status.HTTP_200_OK)
                else:
                    return Response({'mensagem': 'Erro ao enviar o email.', 'erro': f"SendGrid Status Code: {response.status_code}, Body: {response.body}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except Exception as e:
                return Response({'mensagem': 'Erro ao enviar o email.', 'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Views para CMS

class InicioTextoViewSet(viewsets.ModelViewSet):
    queryset = InicioTexto.objects.all()
    serializer_class = InicioTextoSerializer

class InicioImgViewSet(viewsets.ModelViewSet):
    queryset = InicioImg.objects.all()
    serializer_class = InicioImgSerializer

class InicioBgViewSet(viewsets.ModelViewSet):
    queryset = InicioBg.objects.all()
    serializer_class = InicioBgSerializer

class SobreTextoViewSet(viewsets.ModelViewSet):
    queryset = SobreTexto.objects.all()
    serializer_class = SobreTextoSerializer

class SobreImgViewSet(viewsets.ModelViewSet):
    queryset = SobreImg.objects.all()
    serializer_class = SobreImgSerializer

class ComponenteArtigosTextoViewSet(viewsets.ModelViewSet):
    queryset = ComponenteArtigosTexto.objects.all()
    serializer_class = ComponenteArtigosTextoSerializer

class ComponenteContatoTextoViewSet(viewsets.ModelViewSet):
    queryset = ComponenteContatoTexto.objects.all()
    serializer_class = ComponenteContatoTextoSerializer

class PaginaInicioViewSet(viewsets.ModelViewSet):
    queryset = PaginaInicio.objects.all()
    serializer_class = PaginaInicioSerializer

class ComponenteContatoViewSet(viewsets.ModelViewSet):
    queryset = ComponenteContato.objects.all()
    serializer_class = ComponenteContatoSerializer