from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files.storage import default_storage

from javiera.models import Artigo
from javiera.serializers import ArtigoSerializer

# Views para os modelos

class ArtigoViewSet(viewsets.ModelViewSet):
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer

# Views para upload de imagens e PDFs dos artigos (blog)

class UploadImageView(APIView):
    def post(self, request, *args, **kwargs):
        imagem = request.FILES.get('imagem')
        if not imagem:
            return Response({'error': 'Nenhuma imagem enviada.'}, status=status.HTTP_400_BAD_REQUEST)

        nome_arquivo = default_storage.save(f'javiera/blog/imagens/{imagem.name}', imagem)
        url_imagem = default_storage.url(nome_arquivo)

        return Response({'url': url_imagem}, status=status.HTTP_201_CREATED)
    
class UploadPDFView(APIView):
    def post(self, request, *args, **kwargs):
        pdf_file = request.FILES.get('pdf_file')
        if not pdf_file:
            return Response({'error': 'Nenhum arquivo PDF enviado.'}, status=status.HTTP_400_BAD_REQUEST)

        nome_arquivo = default_storage.save(f'javiera/blog/pdfs/{pdf_file.name}', pdf_file)
        url_pdf = default_storage.url(nome_arquivo)

        return Response({'url': url_pdf}, status=status.HTTP_201_CREATED)