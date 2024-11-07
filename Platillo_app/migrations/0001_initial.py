# Generated by Django 5.1 on 2024-11-03 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Catalogo_app', '0001_initial'),
        ('Sucursal_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='platillo_imagenes/')),
                ('catalogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platillos_set', to='Catalogo_app.catalogo')),
            ],
        ),
        migrations.CreateModel(
            name='PlatilloSucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disponibilidad', models.BooleanField(default=True)),
                ('platillo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Platillo_app.platillo')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sucursal_app.sucursal')),
            ],
        ),
        migrations.AddField(
            model_name='platillo',
            name='sucursales',
            field=models.ManyToManyField(through='Platillo_app.PlatilloSucursal', to='Sucursal_app.sucursal'),
        ),
    ]