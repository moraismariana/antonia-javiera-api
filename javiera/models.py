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

# Modelo de teste por enquanto (as acima não foram utilizadas):

class PaginaInicio(DeleteOldImageMixin, SingletonModel):
    introducaoTitulo = models.TextField()
    introducaoSubtitulo = models.TextField()
    sobreTitulo = models.TextField()
    sobreDescricao = models.TextField()
    artigosTitulo = models.TextField()
    artigosDescricao = models.TextField()
    imagem1 = models.ImageField(upload_to='javiera/cms/inicio', null=True, blank=True)
    bg1 = models.ImageField(upload_to='javiera/cms/inicio', null=True, blank=True)
    bg2 = models.ImageField(upload_to='javiera/cms/inicio', null=True, blank=True)

class PaginaSobre(DeleteOldImageMixin, SingletonModel):
    titulo = models.TextField()
    paragrafo1 = models.TextField()
    paragrafo2 = models.TextField()
    imagem1 = models.ImageField(upload_to='javiera/cms/sobre', null=True, blank=True)
    imagem2 = models.ImageField(upload_to='javiera/cms/sobre', null=True, blank=True)

class ComponenteContato(SingletonModel):
    contatoTitulo = models.TextField()
    contatoDescricao = models.TextField()