# Generated by Django 4.2.13 on 2024-06-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_order_order_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_completed',
            field=models.BooleanField(default=False),
        ),
    ]
