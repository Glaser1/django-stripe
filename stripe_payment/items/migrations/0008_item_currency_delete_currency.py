# Generated by Django 4.1.6 on 2023-02-17 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_currency_country_currency_name_alter_currency_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(default='$', help_text='Укажите название валюты', max_length=50, verbose_name='Валюта'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Currency',
        ),
    ]
