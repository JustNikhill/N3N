# Generated by Django 4.2 on 2023-04-11 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_article_publishdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
