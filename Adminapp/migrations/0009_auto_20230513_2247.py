# Generated by Django 3.2.18 on 2023-05-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0008_services_subservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subservice',
            name='service_name',
            field=models.CharField(choices=[('haircut', 'Haircut'), ('wax', 'Wax'), ('facial', 'Facial')], max_length=20),
        ),
        migrations.AlterField(
            model_name='subservice',
            name='service_type',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]
