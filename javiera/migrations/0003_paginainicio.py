# Generated by Django 5.1.6 on 2025-02-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('javiera', '0002_componenteartigostexto_componentecontatotexto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaginaInicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introducaoTitulo', models.TextField()),
                ('introducaoSubtitulo', models.TextField()),
                ('sobreTitulo', models.TextField()),
                ('sobreDescricao', models.TextField()),
                ('artigosTitulo', models.TextField()),
                ('artigosDescricao', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
