# Generated by Django 4.2.5 on 2023-09-17 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_remove_orders_manager_remove_orders_order_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]