# Generated by Django 5.1 on 2024-11-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sucursal_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursal',
            name='estado',
            field=models.CharField(default='activo', max_length=20),
        ),
        migrations.AddField(
            model_name='sucursal',
            name='imagen',
            field=models.ImageField(default='200x200.png', upload_to='sucursal_imagenes/'),
        ),
    ]
