from rest_framework import serializers
from javiera.models import Artigo, PaginaInicio, PaginaSobre,ComponenteContato

class ArtigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artigo
        fields = '__all__'

class FormularioContatoSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    mensagem = serializers.CharField()

# Serializers CMS

class PaginaInicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaginaInicio
        fields = "__all__"

class PaginaSobreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaginaSobre
        fields = "__all__"

class ComponenteContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponenteContato
        fields = "__all__"
