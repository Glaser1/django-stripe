# Generated by Django 4.1.6 on 2023-02-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_alter_item_currency_alter_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(help_text='Укажите цену товара (в центах)', verbose_name='Цена'),
        ),
    ]
