# Generated by Django 4.2.1 on 2023-05-25 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PadelApp', '0006_remove_comentario_fecha_actualizacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='imagen',
        ),
    ]
