# Generated by Django 4.1.4 on 2023-10-06 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mystore", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.IntegerField(),
        ),
    ]
