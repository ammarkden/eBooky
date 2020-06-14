# Generated by Django 3.0.5 on 2020-05-20 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileIcon', models.ImageField(blank=True, null=True, upload_to='library/usericons')),
                ('profileNumber', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='deliveryprocess',
            name='DeliverPerson',
        ),
        migrations.RemoveField(
            model_name='deliveryprocess',
            name='choosedBook',
        ),
        migrations.RemoveField(
            model_name='deliveryprocess',
            name='userName',
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Cat_Books', to='library.Category'),
        ),
        migrations.DeleteModel(
            name='DeliveryPerson',
        ),
        migrations.DeleteModel(
            name='DeliveryProcess',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
