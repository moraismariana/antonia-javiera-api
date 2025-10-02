from rest_framework import serializers
from francoadv.models import PaginaInicio, PaginaSobre, PaginaServicos, ComponenteInsta, ComponenteContato, ComponenteCTA, Servico, Artigo

class ArtigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artigo
        fields = '__all__'

# CMS
class PaginaInicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaginaInicio
        fields = '__all__'

class PaginaSobreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaginaSobre
        fields = '__all__'

class PaginaServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaginaServicos
        fields = '__all__'

class ComponenteInstaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponenteInsta
        fields = '__all__'

class ComponenteContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponenteContato
        fields = '__all__'

class ComponenteCTASerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponenteCTA
        fields = '__all__'

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'

# Formulário Contato
class FormularioContatoSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    telefone = serializers.CharField(max_length=20)
    mensagem = serializers.CharField()