# Generated by Django 3.2.18 on 2023-05-31 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0008_auto_20230530_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
