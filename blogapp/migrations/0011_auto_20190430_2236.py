# Generated by Django 2.2 on 2019-05-01 03:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_auto_20190430_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
