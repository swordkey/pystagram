# Generated by Django 3.2.3 on 2021-05-31 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20210531_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='userid',
        ),
    ]