# Generated by Django 2.2 on 2019-05-01 02:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_auto_20190430_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='disable_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]