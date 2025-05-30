from django.urls import path, include
from rest_framework import routers

from francoadv.views import PaginaInicioViewSet, PaginaSobreViewSet, PaginaServicosViewSet, ComponenteInstaViewSet, ComponenteContatoViewSet, ComponenteCTAViewSet, ServicoViewSet, FormularioContatoViewSet, UserDetailsView

router_francoadv = routers.DefaultRouter()

router_francoadv.register('paginainicio', PaginaInicioViewSet, basename='paginainicio')
router_francoadv.register('paginasobre', PaginaSobreViewSet, basename='paginasobre')
router_francoadv.register('paginaservicos', PaginaServicosViewSet, basename='paginaservicos')
router_francoadv.register('componenteinsta', ComponenteInstaViewSet, basename='componenteinsta')
router_francoadv.register('componentecontato', ComponenteContatoViewSet, basename='componentecontato')
router_francoadv.register('componentecta', ComponenteCTAViewSet, basename='componentecta')
router_francoadv.register('servicos', ServicoViewSet, basename='servicos')
router_francoadv.register('contato', FormularioContatoViewSet, basename='contato')

urlpatterns = [
    path('', include(router_francoadv.urls)),
    path('userdetails/', UserDetailsView.as_view(), name='userdetails'),
]