# Generated by Django 5.1 on 2024-11-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaWeb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.CharField(default='activo', max_length=25),
        ),
    ]
