# Generated by Django 4.2.6 on 2023-10-29 05:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventario", "0003_alter_productos_cantidad"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productos",
            name="cantidad",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="productos",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="productos",
            name="nombre",
            field=models.CharField(max_length=50),
        ),
    ]
