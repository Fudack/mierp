# Generated by Django 4.2.6 on 2023-10-29 06:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("inventario", "0005_remove_productos_cantidad_productos_fechasalida_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productos",
            name="fechaSalida",
        ),
        migrations.RemoveField(
            model_name="productos",
            name="imagen",
        ),
        migrations.AddField(
            model_name="productos",
            name="cantidad",
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
