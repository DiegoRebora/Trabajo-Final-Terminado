# Generated by Django 4.2.1 on 2023-05-23 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PadelApp', '0003_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='comentarios/'),
        ),
    ]
