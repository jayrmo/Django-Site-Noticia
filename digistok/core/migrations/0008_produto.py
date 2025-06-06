# Generated by Django 5.2.1 on 2025-06-04 19:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_categoria_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True)),
                ('descricao', models.CharField(max_length=200)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='produtos/')),
                ('unidade_medida', models.CharField(max_length=200)),
                ('detalhes', models.TextField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.fornecedor')),
            ],
        ),
    ]
