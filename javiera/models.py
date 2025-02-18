from django.db import models
from django.core.exceptions import ValidationError
from javiera.mixins import DeleteOldImageMixin

# Classe para artigos do blog
class Artigo(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    descricao = models.TextField(verbose_name='Descrição')
    fixado = models.BooleanField(default=False, verbose_name='Fixado')
    conteudo = models.TextField(verbose_name='Conteúdo do Artigo (Quill.js)')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'

# Classes para edição de conteúdo CMS
class SingletonModel(models.Model):
    """Classe abstrata para garantir que apenas uma instância do modelo exista."""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError(f"Já existe uma instância de {self.__class__.__name__}.")
        super().save(*args, **kwargs)

class InicioTexto(SingletonModel):
    introducao_titulo = models.TextField()
    introducao_subtitulo = models.TextField()
    sobre_titulo = models.TextField()
    sobre_descricao = models.TextField()

class InicioImg(DeleteOldImageMixin, SingletonModel):
    sobre = models.ImageField(upload_to='javiera/cms/inicio')

class InicioBg(DeleteOldImageMixin, SingletonModel):
    introducao = models.ImageField(upload_to='javiera/cms/inicio')
    artigos = models.ImageField(upload_to='javiera/cms/inicio')

class SobreTexto(SingletonModel):
    titulo = models.TextField()
    paragrafo_1 = models.TextField()
    paragrafo_2 = models.TextField()

class SobreImg(DeleteOldImageMixin, SingletonModel):
    imagem_1 = models.ImageField(upload_to='javiera/cms/sobre')
    imagem_2 = models.ImageField(upload_to='javiera/cms/sobre')

class ComponenteArtigosTexto(SingletonModel):
    artigos_titulo = models.TextField()
    artigos_descricao = models.TextField()

class ComponenteContatoTexto(SingletonModel):
    contato_titulo = models.TextField()
    contato_descricao = models.TextField()