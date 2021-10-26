# Generated by Django 3.2.8 on 2021-10-19 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False, verbose_name='Product ID')),
                ('name', models.CharField(max_length=40, verbose_name="Product's Name")),
                ('brand', models.CharField(max_length=40, verbose_name="Product's Brand")),
                ('price', models.FloatField(verbose_name="Product's Price")),
                ('qty', models.IntegerField(default=1, verbose_name='Quantity')),
                ('warranty', models.IntegerField(default=1, verbose_name='Warranty in Year')),
                ('delivery', models.CharField(default='India', max_length=40, verbose_name='Delivery Country')),
                ('pic', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
