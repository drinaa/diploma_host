# Generated by Django 3.1.7 on 2021-05-16 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diploma_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='points',
            name='code',
            field=models.CharField(max_length=4),
        ),
    ]