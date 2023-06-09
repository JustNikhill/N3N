# Generated by Django 4.2 on 2023-04-11 10:45

import datetime
from django.db import migrations, models
import portfolio.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=portfolio.utils.upload_picture)),
                ('writer', models.CharField(default='Nima', max_length=200)),
                ('publishDate', models.DateTimeField(default=datetime.datetime.now)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]
