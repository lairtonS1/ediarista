# Generated by Django 3.2.8 on 2021-10-12 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diarista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=11)),
                ('lougradouro', models.CharField(max_length=60)),
                ('mumero', models.IntegerField()),
                ('bairro', models.CharField(max_length=30)),
                ('complemento', models.CharField(blank=True, max_length=30)),
                ('cep', models.CharField(max_length=14)),
                ('estado', models.CharField(max_length=2)),
                ('codigo_ibge', models.IntegerField()),
                ('foto_usuario', models.ImageField(upload_to='')),
            ],
        ),
    ]
