# Generated by Django 4.2.1 on 2023-06-02 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0003_merge_0002_detsale_fpago_0002_sale_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detsale',
            name='fpago',
        ),
        migrations.AddField(
            model_name='sale',
            name='fpago',
            field=models.CharField(choices=[('e', 'Efectivo'), ('te', 'Transferencia Electronica'), ('tb', 'Transferencia Bancarias'), ('c', 'Cheques')], default='Efectivo', max_length=100),
        ),
    ]
