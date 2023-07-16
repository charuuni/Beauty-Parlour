# Generated by Django 3.2.18 on 2023-05-31 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0009_alter_cart_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='cartid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Userapp.cart'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Userapp.register'),
        ),
    ]