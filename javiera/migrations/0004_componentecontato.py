# Generated by Django 5.1.6 on 2025-02-18 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('javiera', '0003_paginainicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponenteContato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contatoTitulo', models.TextField()),
                ('contatoDescricao', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
