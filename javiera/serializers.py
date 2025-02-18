from rest_framework import serializers
from javiera.models import Artigo, InicioTexto, InicioImg, InicioBg, SobreTexto, SobreImg, ComponenteArtigosTexto, ComponenteContatoTexto

class ArtigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artigo
        fields = '__all__'

class FormularioContatoSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    mensagem = serializers.CharField()


# Serializers CMS

class InicioTextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioTexto
        fields = "__all__"

class InicioImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioImg
        fields = "__all__"

class InicioBgSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioBg
        fields = "__all__"

class SobreTextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SobreTexto
        fields = "__all__"

class SobreImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = SobreImg
        fields = "__all__"

class ComponenteArtigosTextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponenteArtigosTexto
        fields = "__all__"

class ComponenteContatoTextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponenteContatoTexto
        fields = "__all__"