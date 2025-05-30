# Generated by Django 5.1.6 on 2025-05-14 19:51

import francoadv.mixins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComponenteContato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contatoTitulo', models.TextField()),
                ('contatoTexto1', models.TextField()),
                ('contatoTexto2', models.TextField()),
                ('contatoSubtitulo', models.TextField()),
                ('contatoTexto3', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ComponenteCTA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctaTitulo', models.TextField()),
                ('bg', models.ImageField(blank=True, null=True, upload_to='javiera/cms/inicio')),
            ],
            options={
                'abstract': False,
            },
            bases=(francoadv.mixins.DeleteOldImageMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ComponenteInsta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instaTitulo', models.TextField()),
                ('instaTexto', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaginaInicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introTitulo', models.TextField()),
                ('introSubtitulo', models.TextField()),
                ('ctaTitulo', models.TextField()),
                ('ctaSubtitulo', models.TextField()),
                ('beneficiosTitulo', models.TextField()),
                ('beneficio1Titulo', models.TextField()),
                ('beneficio1Texto', models.TextField()),
                ('beneficio2Titulo', models.TextField()),
                ('beneficio2Texto', models.TextField()),
                ('beneficio3Titulo', models.TextField()),
                ('beneficio3Texto', models.TextField()),
                ('processoTitulo', models.TextField()),
                ('processo1Titulo', models.TextField()),
                ('processo1Texto', models.TextField()),
                ('processo2Titulo', models.TextField()),
                ('processo2Texto', models.TextField()),
                ('processo3Titulo', models.TextField()),
                ('processo3Texto', models.TextField()),
                ('areasAtuacaoTitulo', models.TextField()),
                ('areasAtuacaoTexto', models.TextField()),
                ('fundadoraTitulo', models.TextField()),
                ('fundadoraSubtitulo', models.TextField()),
                ('fundadoraTexto', models.TextField()),
                ('imagem1', models.ImageField(blank=True, null=True, upload_to='francoadv/cms/inicio')),
                ('bg1', models.ImageField(blank=True, null=True, upload_to='javiera/cms/inicio')),
                ('bg2', models.ImageField(blank=True, null=True, upload_to='javiera/cms/inicio')),
            ],
            options={
                'abstract': False,
            },
            bases=(francoadv.mixins.DeleteOldImageMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PaginaServicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paginaTitulo', models.TextField()),
                ('advocaciaTitulo', models.TextField()),
                ('advocaciaSubtitulo', models.TextField()),
                ('advocaciaTexto', models.TextField()),
                ('areasTitulo', models.TextField()),
                ('areasSubtitulo', models.TextField()),
                ('areasTexto', models.TextField()),
                ('areas2Titulo1', models.TextField()),
                ('areas2Texto1', models.TextField()),
                ('areas2Titulo2', models.TextField()),
                ('areas2Texto2', models.TextField()),
                ('areas2Titulo3', models.TextField()),
                ('areas2Texto3', models.TextField()),
                ('areas2Titulo4', models.TextField()),
                ('areas2Texto4', models.TextField()),
                ('tratamentoTitulo', models.TextField()),
                ('tratamentoSubtitulo', models.TextField()),
                ('tratamentoTexto', models.TextField()),
                ('bg', models.ImageField(blank=True, null=True, upload_to='javiera/cms/inicio')),
            ],
            options={
                'abstract': False,
            },
            bases=(francoadv.mixins.DeleteOldImageMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PaginaSobre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paginaTitulo', models.TextField()),
                ('sobreTitulo', models.TextField()),
                ('sobreTexto', models.TextField()),
                ('diferenciaisTitulo', models.TextField()),
                ('diferenciaisTexto2', models.TextField()),
                ('diferenciaisTexto3', models.TextField()),
                ('diferenciaisTexto4', models.TextField()),
                ('diferenciaisTexto5', models.TextField()),
                ('diferenciaisTexto6', models.TextField()),
                ('diferenciaisTexto1', models.TextField()),
                ('advogadaTitulo', models.TextField()),
                ('advogadaTexto1', models.TextField()),
                ('advogadaTexto2', models.TextField()),
                ('advogadaTexto3', models.TextField()),
                ('especialistasTitulo', models.TextField()),
                ('especialistasTexto', models.TextField()),
                ('especialistasItem1', models.TextField()),
                ('especialistasItem2', models.TextField()),
                ('especialistasItem3', models.TextField()),
                ('imagem1', models.ImageField(blank=True, null=True, upload_to='francoadv/cms/inicio')),
            ],
            options={
                'abstract': False,
            },
            bases=(francoadv.mixins.DeleteOldImageMixin, models.Model),
        ),
    ]
