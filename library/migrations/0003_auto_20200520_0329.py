# Generated by Django 3.0.5 on 2020-05-20 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20200520_0224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profileNumber',
            new_name='phoneNumber',
        ),
    ]
