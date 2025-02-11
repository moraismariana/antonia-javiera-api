from django.urls import path, include
from javiera.views import ArtigoViewSet, UploadImageView, UploadPDFView
from rest_framework import routers

router_javiera = routers.DefaultRouter()
router_javiera.register('artigos', ArtigoViewSet, basename='artigos')

urlpatterns = [
    path('', include(router_javiera.urls)),
    path('blog/imagem/', UploadImageView.as_view(), name='blog-imagem'),
    path('blog/pdf/', UploadPDFView.as_view(), name='blog-pdf'),
]