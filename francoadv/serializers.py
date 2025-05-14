from rest_framework import serializers
from francoadv.models import PaginaInicio, PaginaSobre, PaginaServicos, ComponenteInsta, ComponenteContato, ComponenteCTA
# from javiera.models import Artigo, PaginaInicio, PaginaSobre,ComponenteContato

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