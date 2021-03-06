# Generated by Django 3.2.3 on 2021-05-26 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20210526_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='content',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='filtered_image',
            field=models.ImageField(upload_to='%Y/%m/%d/filtered'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='%Y/%m/%d/orig'),
        ),
    ]
