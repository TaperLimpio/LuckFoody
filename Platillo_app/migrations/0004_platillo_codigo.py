# Generated by Django 5.1 on 2024-11-15 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Platillo_app', '0003_alter_platillo_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='platillo',
            name='codigo',
            field=models.CharField(default=1, max_length=13),
        ),
    ]
