# Generated by Django 4.2.2 on 2023-08-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_order_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
