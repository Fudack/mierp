# Generated by Django 4.2.6 on 2023-10-29 06:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "inventario",
            "0006_remove_productos_fechasalida_remove_productos_imagen_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="productos",
            name="cantidad",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]