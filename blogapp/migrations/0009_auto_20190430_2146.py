# Generated by Django 2.2 on 2019-05-01 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_auto_20190430_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='post',
            name='is_disabled',
        ),
    ]
