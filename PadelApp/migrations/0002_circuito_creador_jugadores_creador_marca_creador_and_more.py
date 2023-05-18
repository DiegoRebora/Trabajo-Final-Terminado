# Generated by Django 4.2.1 on 2023-05-17 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PadelApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='circuito',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='jugadores',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='marca',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='circuito',
            name='cant_torneos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jugadores',
            name='edad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='jugadores',
            name='marca',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
