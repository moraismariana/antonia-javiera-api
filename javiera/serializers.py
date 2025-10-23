from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from javiera.models import Artigo, PaginaInicio, PaginaSobre,ComponenteContato, Curso, Aula

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

# Cursos e Aulas

class AulaPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

class AulaResumidaSerializer(serializers.ModelSerializer):
    """
    Serializer para a representação resumida de uma Aula.
    """
    class Meta:
        model = Aula
        fields = ['id', 'titulo', 'descricao']

class CursoDetalhadoSerializer(serializers.ModelSerializer):
    """
    Serializer para a representação detalhada de um Curso,
    incluindo a lista paginada e pesquisável de suas aulas.
    """
    aulas = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = ['id', 'nome', 'descricao', 'banner', 'aulas']

    def get_aulas(self, obj):
        paginator = AulaPagination()

        request = self.context.get('request')

        queryset = obj.aulas.all().order_by('data_criacao')

        query_param = request.query_params.get('q')
        if query_param:
            queryset = queryset.filter(
                Q(titulo__icontains=query_param) | Q(descricao__icontains=query_param)
            )
        
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        
        serializer = AulaResumidaSerializer(paginated_queryset, many=True)

        return paginator.get_paginated_response(serializer.data).data

class CursoResumidoSerializer(serializers.ModelSerializer):
    """
    Serializer para a representação resumida de um Curso.
    """
    class Meta:
        model = Curso
        fields = ['id', 'nome', 'descricao']

class AulaDetalhadaSerializer(serializers.ModelSerializer):
    """
    Serializer para a representação detalhada de uma Aula.
    """
    class Meta:
        model = Aula
        fields = '__all__'