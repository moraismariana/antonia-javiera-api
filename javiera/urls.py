from django.urls import path, include
from rest_framework import routers

from javiera.views import ArtigoViewSet, FormularioContatoViewSet

router_javiera = routers.DefaultRouter()
router_javiera.register('artigos', ArtigoViewSet, basename='artigos')
router_javiera.register('contato', FormularioContatoViewSet, basename='contato')

urlpatterns = [
    path('', include(router_javiera.urls)),
]