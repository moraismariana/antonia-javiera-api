from django.urls import path, include
from rest_framework import routers

from javiera.views import ArtigoViewSet, FormularioContatoViewSet, InicioTextoViewSet, InicioImgViewSet, InicioBgViewSet, SobreTextoViewSet, SobreImgViewSet, ComponenteArtigosTextoViewSet, ComponenteContatoTextoViewSet, PaginaInicioViewSet, ComponenteContatoViewSet

router_javiera = routers.DefaultRouter()
router_javiera.register('artigos', ArtigoViewSet, basename='artigos')
router_javiera.register('contato', FormularioContatoViewSet, basename='contato')
router_javiera.register('iniciotexto', InicioTextoViewSet, basename='iniciotexto')
router_javiera.register('inicioimg', InicioImgViewSet, basename='inicioimg')
router_javiera.register('iniciobg', InicioBgViewSet, basename='iniciobg')
router_javiera.register('sobretexto', SobreTextoViewSet, basename='sobretexto')
router_javiera.register('sobreimg', SobreImgViewSet, basename='sobreimg')
router_javiera.register('componenteartigostexto', ComponenteArtigosTextoViewSet, basename='componenteartigostexto')
router_javiera.register('componentecontatotexto', ComponenteContatoTextoViewSet, basename='componentecontatotexto')
router_javiera.register('paginainicio', PaginaInicioViewSet, basename='paginainicio')
router_javiera.register('componentecontato', ComponenteContatoViewSet, basename='componentecontato')

urlpatterns = [
    path('', include(router_javiera.urls)),
]