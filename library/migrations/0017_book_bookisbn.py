# Generated by Django 3.0.5 on 2020-06-12 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_auto_20200612_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookISBN',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
