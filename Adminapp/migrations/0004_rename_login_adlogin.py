# Generated by Django 3.2.18 on 2023-05-08 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0003_rename_adminlogin_login'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='login',
            new_name='Adlogin',
        ),
    ]