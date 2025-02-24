from django.urls import path, include
from rest_framework import routers

from javiera.views import ArtigoViewSet, FormularioContatoViewSet, PaginaInicioViewSet, PaginaSobreViewSet, ComponenteContatoViewSet, UserDetailsView

router_javiera = routers.DefaultRouter()
router_javiera.register('artigos', ArtigoViewSet, basename='artigos')
router_javiera.register('contato', FormularioContatoViewSet, basename='contato')

router_javiera.register('paginainicio', PaginaInicioViewSet, basename='paginainicio')
router_javiera.register('paginasobre', PaginaSobreViewSet, basename='paginasobre')
router_javiera.register('componentecontato', ComponenteContatoViewSet, basename='componentecontato')

urlpatterns = [
    path('', include(router_javiera.urls)),
    path('userdetails/', UserDetailsView.as_view(), name='userdetails'),
]