# Generated by Django 5.0.4 on 2024-05-01 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_mensajessoporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajessoporte',
            name='adjuntos',
            field=models.ImageField(upload_to='myapp/static/imagenes_soporte/'),
        ),
    ]
