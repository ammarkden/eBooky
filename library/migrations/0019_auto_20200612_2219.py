# Generated by Django 3.0.5 on 2020-06-12 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_auto_20200612_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookWiki',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='bookDetails',
            field=models.TextField(blank=True, null=True),
        ),
    ]
