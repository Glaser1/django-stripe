# Generated by Django 4.1.6 on 2023-02-17 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_order_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currencies', to='items.item')),
            ],
        ),
    ]
