# Generated by Django 3.2.18 on 2023-05-26 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0012_auto_20230515_1302'),
        ('Userapp', '0003_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('serviceid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminapp.service')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Userapp.register')),
            ],
        ),
    ]
