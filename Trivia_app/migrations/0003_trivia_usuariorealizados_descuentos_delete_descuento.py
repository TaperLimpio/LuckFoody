# Generated by Django 5.1 on 2024-12-01 19:47

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trivia_app', '0002_rename_nombre_trivia_titulo'),
        ('Usuario_app', '0002_usuario_rut'),
    ]

    operations = [
        migrations.AddField(
            model_name='trivia',
            name='usuarioRealizados',
            field=models.ManyToManyField(related_name='Mis_trivias', to='Usuario_app.usuario'),
        ),
        migrations.CreateModel(
            name='Descuentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCreacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaTermino', models.DateTimeField()),
                ('valor', models.FloatField(default=0.0, null=True)),
                ('porcentajeCorrecto', models.FloatField(default=0.0)),
                ('id_trivia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='descuento', to='Trivia_app.trivia')),
                ('usuPropietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descuentos', to='Usuario_app.usuario')),
            ],
        ),
        migrations.DeleteModel(
            name='Descuento',
        ),
    ]