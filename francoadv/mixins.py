from django.db.models import ImageField
from django.db.models.signals import pre_delete
from django.dispatch import receiver

class DeleteOldImageMixin:
    """Mixin para deletar imagens antigas ao atualizar ou deletar o objeto."""

    def delete_old_images(self):
        """Deleta todas as imagens associadas ao objeto."""
        for field in self._get_image_fields():
            imagem = getattr(self, field)
            if imagem:
                imagem.delete(save=False)

    def _get_image_fields(self):
        """Retorna uma lista dos nomes dos campos de imagem do objeto."""
        return [
            field.name for field in self._meta.fields
            if isinstance(field, ImageField)
        ]

    def save(self, *args, **kwargs):
        """Sobrescreve o método save para deletar imagens antigas ao atualizar o objeto."""
        if self.pk:
            old_instance = self.__class__.objects.get(pk=self.pk)
            for field in self._get_image_fields():
                nova_imagem = getattr(self, field)
                imagem_antiga = getattr(old_instance, field)
                if imagem_antiga and imagem_antiga != nova_imagem:
                    imagem_antiga.delete(save=False)

        super().save(*args, **kwargs)

# Sinal para deletar imagens ao deletar o objeto
@receiver(pre_delete)
def delete_images_on_delete(sender, instance, **kwargs):
    if isinstance(instance, DeleteOldImageMixin):
        instance.delete_old_images()
