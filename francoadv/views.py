from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from francoadv.models import PaginaInicio, PaginaSobre, PaginaServicos, ComponenteInsta, ComponenteContato, ComponenteCTA

from francoadv.serializers import PaginaInicioSerializer, PaginaSobreSerializer, PaginaServicosSerializer, ComponenteInstaSerializer, ComponenteContatoSerializer, ComponenteCTASerializer

class PaginaInicioViewSet(viewsets.ModelViewSet):
    queryset = PaginaInicio.objects.all()
    serializer_class = PaginaInicioSerializer
    permission_classes = [AllowAny]

class PaginaSobreViewSet(viewsets.ModelViewSet):
    queryset = PaginaSobre.objects.all()
    serializer_class = PaginaSobreSerializer
    permission_classes = [AllowAny]

class PaginaServicosViewSet(viewsets.ModelViewSet):
    queryset = PaginaServicos.objects.all()
    serializer_class = PaginaServicosSerializer
    permission_classes = [AllowAny]

class ComponenteInstaViewSet(viewsets.ModelViewSet):
    queryset = ComponenteInsta.objects.all()
    serializer_class = ComponenteInstaSerializer
    permission_classes = [AllowAny]

class ComponenteContatoViewSet(viewsets.ModelViewSet):
    queryset = ComponenteContato.objects.all()
    serializer_class = ComponenteContatoSerializer
    permission_classes = [AllowAny]

class ComponenteCTAViewSet(viewsets.ModelViewSet):
    queryset = ComponenteCTA.objects.all()
    serializer_class = ComponenteCTASerializer
    permission_classes = [AllowAny]