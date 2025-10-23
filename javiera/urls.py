from django.urls import path, include
from rest_framework import routers

from javiera.views import ArtigoViewSet, FormularioContatoViewSet, PaginaInicioViewSet, PaginaSobreViewSet, ComponenteContatoViewSet, UserDetailsView, CursoViewSet, AulaViewSet

app_name = 'javiera'

router_javiera = routers.DefaultRouter()
router_javiera.register('artigos', ArtigoViewSet, basename='artigos')
router_javiera.register('contato', FormularioContatoViewSet, basename='contato')

router_javiera.register('paginainicio', PaginaInicioViewSet, basename='paginainicio')
router_javiera.register('paginasobre', PaginaSobreViewSet, basename='paginasobre')
router_javiera.register('componentecontato', ComponenteContatoViewSet, basename='componentecontato')

router_javiera.register('cursos', CursoViewSet, basename='cursos')
router_javiera.register('aulas', AulaViewSet, basename='aulas')

urlpatterns = [
    path('', include(router_javiera.urls)),
    path('userdetails/', UserDetailsView.as_view(), name='userdetails'),
]