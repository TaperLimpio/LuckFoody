# Generated by Django 5.1 on 2024-11-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogo',
            name='estado',
            field=models.CharField(default='Desactivado', max_length=20),
        ),
    ]