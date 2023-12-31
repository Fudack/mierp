# Generated by Django 4.2.6 on 2023-10-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventario", "0001_initial"),
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
            field=models.IntegerField(blank=True, default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name="productos",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name="productos",
            name="nombre",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
