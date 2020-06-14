# Generated by Django 3.0.5 on 2020-05-21 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20200520_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='favBooks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='isfavBook',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
