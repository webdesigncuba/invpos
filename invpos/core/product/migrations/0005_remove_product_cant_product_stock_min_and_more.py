# Generated by Django 4.2.1 on 2023-05-24 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_cant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cant',
        ),
        migrations.AddField(
            model_name='product',
            name='stock_min',
            field=models.IntegerField(default=1, verbose_name='Stock Minimo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='Cantidad Inicial'),
        ),
    ]
