# Generated by Django 4.2.1 on 2023-05-22 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category.category', verbose_name='Categoría'),
        ),
    ]
