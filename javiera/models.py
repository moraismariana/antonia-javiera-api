from django.db import models

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