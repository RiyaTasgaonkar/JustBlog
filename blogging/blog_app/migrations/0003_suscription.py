# Generated by Django 3.1.3 on 2020-11-20 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0002_auto_20201115_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=3)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Rather Not Say')], default='M', max_length=20)),
                ('frequency', models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly'), ('MT', 'Monthly')], default='D', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]