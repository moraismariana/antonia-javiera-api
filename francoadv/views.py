from rest_framework import viewsets

from francoadv.models import PaginaInicio, PaginaSobre, PaginaServicos, ComponenteInsta, ComponenteContato, ComponenteCTA

from francoadv.serializers import PaginaInicioSerializer, PaginaSobreSerializer, PaginaServicosSerializer, ComponenteInstaSerializer, ComponenteContatoSerializer, ComponenteCTASerializer

class PaginaInicioViewSet(viewsets.ModelViewSet):
    queryset = PaginaInicio.objects.all()
    serializer_class = PaginaInicioSerializer

class PaginaSobreViewSet(viewsets.ModelViewSet):
    queryset = PaginaSobre.objects.all()
    serializer_class = PaginaSobreSerializer

class PaginaServicosViewSet(viewsets.ModelViewSet):
    queryset = PaginaServicos.objects.all()
    serializer_class = PaginaServicosSerializer

class ComponenteInstaViewSet(viewsets.ModelViewSet):
    queryset = ComponenteInsta.objects.all()
    serializer_class = ComponenteInstaSerializer

class ComponenteContatoViewSet(viewsets.ModelViewSet):
    queryset = ComponenteContato.objects.all()
    serializer_class = ComponenteContatoSerializer

class ComponenteCTAViewSet(viewsets.ModelViewSet):
    queryset = ComponenteCTA.objects.all()
    serializer_class = ComponenteCTASerializer