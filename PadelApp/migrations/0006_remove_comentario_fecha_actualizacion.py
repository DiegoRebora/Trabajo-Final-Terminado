# Generated by Django 4.2.1 on 2023-05-23 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PadelApp', '0005_remove_comentario_objeto_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='fecha_actualizacion',
        ),
    ]
