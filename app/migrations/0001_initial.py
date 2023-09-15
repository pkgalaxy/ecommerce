# Generated by Django 4.2.2 on 2023-08-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, null=True)),
                ('product_details', models.TextField(max_length=150, null=True)),
                ('product_price', models.TextField(max_length=10, null=True)),
                ('product_image', models.ImageField(null=True, upload_to='product-images')),
            ],
        ),
    ]