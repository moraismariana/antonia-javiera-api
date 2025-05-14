from django.db import models
from django.core.exceptions import ValidationError
from francoadv.mixins import DeleteOldImageMixin

# Classes para edição de conteúdo CMS
class SingletonModel(models.Model):
    """Classe abstrata para garantir que apenas uma instância do modelo exista."""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError(f"Já existe uma instância de {self.__class__.__name__}.")
        super().save(*args, **kwargs)

class PaginaInicio(DeleteOldImageMixin, SingletonModel):
    introTitulo = models.TextField()
    introSubtitulo = models.TextField()
    ctaTitulo = models.TextField()
    ctaSubtitulo = models.TextField()
    beneficiosTitulo = models.TextField()
    beneficio1Titulo = models.TextField()
    beneficio1Texto = models.TextField()
    beneficio2Titulo = models.TextField()
    beneficio2Texto = models.TextField()
    beneficio3Titulo = models.TextField()
    beneficio3Texto = models.TextField()
    processoTitulo = models.TextField()
    processo1Titulo = models.TextField()
    processo1Texto = models.TextField()
    processo2Titulo = models.TextField()
    processo2Texto = models.TextField()
    processo3Titulo = models.TextField()
    processo3Texto = models.TextField()
    processo4Titulo = models.TextField()
    processo4Texto = models.TextField()
    areasAtuacaoTitulo = models.TextField()
    areasAtuacaoTexto = models.TextField()
    fundadoraTitulo = models.TextField()
    fundadoraSubtitulo = models.TextField()
    fundadoraTexto = models.TextField()
    imagem1 = models.ImageField(upload_to='francoadv/cms/inicio', null=True, blank=True)
    bg1 = models.ImageField(upload_to='francoadv/cms/inicio', null=True, blank=True)
    bg2 = models.ImageField(upload_to='francoadv/cms/inicio', null=True, blank=True)

class PaginaSobre(DeleteOldImageMixin, SingletonModel):
    paginaTitulo = models.TextField()
    sobreTitulo = models.TextField()
    sobreTexto = models.TextField()
    diferenciaisTitulo = models.TextField()
    diferenciaisTexto1 = models.TextField()
    diferenciaisTexto2 = models.TextField()
    diferenciaisTexto3 = models.TextField()
    diferenciaisTexto4 = models.TextField()
    diferenciaisTexto5 = models.TextField()
    diferenciaisTexto6 = models.TextField()
    diferenciaisTexto1 = models.TextField()
    advogadaTitulo = models.TextField()
    advogadaTexto1 = models.TextField()
    advogadaTexto2 = models.TextField()
    advogadaTexto3 = models.TextField()
    especialistasTitulo = models.TextField()
    especialistasTexto = models.TextField()
    especialistasItem1 = models.TextField()
    especialistasItem2 = models.TextField()
    especialistasItem3 = models.TextField()
    imagem1 = models.ImageField(upload_to='francoadv/cms/sobre', null=True, blank=True)

class PaginaServicos(DeleteOldImageMixin, SingletonModel):
    paginaTitulo = models.TextField()
    advocaciaTitulo = models.TextField()
    advocaciaSubtitulo = models.TextField()
    advocaciaTexto = models.TextField()
    areasTitulo = models.TextField()
    areasSubtitulo = models.TextField()
    areasTexto = models.TextField()
    areas2Titulo1 = models.TextField()
    areas2Texto1 = models.TextField()
    areas2Titulo2  = models.TextField()
    areas2Texto2 = models.TextField()
    areas2Titulo3 = models.TextField()
    areas2Texto3 = models.TextField()
    areas2Titulo4 = models.TextField()
    areas2Texto4 = models.TextField()
    tratamentoTitulo = models.TextField()
    tratamentoSubtitulo = models.TextField()
    tratamentoTexto = models.TextField()
    bg = models.ImageField(upload_to='francoadv/cms/servicos', null=True, blank=True)

class ComponenteInsta(SingletonModel):
    instaTitulo = models.TextField()
    instaTexto = models.TextField()

class ComponenteContato(SingletonModel):
    contatoTitulo = models.TextField()
    contatoTexto1 = models.TextField()
    contatoTexto2 = models.TextField()
    contatoSubtitulo = models.TextField()
    contatoTexto3 = models.TextField()

class ComponenteCTA(DeleteOldImageMixin, SingletonModel):
    ctaTitulo = models.TextField()
    bg = models.ImageField(upload_to='francoadv/cms/cta', null=True, blank=True)