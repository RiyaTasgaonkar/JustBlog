# Generated by Django 3.1.3 on 2020-11-20 07:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0004_auto_20201120_1050'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Suscription',
            new_name='Subscription',
        ),
    ]
