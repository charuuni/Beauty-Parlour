# Generated by Django 3.2.18 on 2023-05-14 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0010_auto_20230515_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subservice',
            name='services',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Adminapp.service'),
        ),
    ]
