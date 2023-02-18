# Generated by Django 4.1.6 on 2023-02-17 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_item_options_order_items_delete_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='items', to='items.item'),
        ),
    ]
