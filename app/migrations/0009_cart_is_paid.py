# Generated by Django 4.2.2 on 2023-08-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_cart_is_paid_alter_cart_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
