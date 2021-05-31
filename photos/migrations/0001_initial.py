# Generated by Django 3.2.3 on 2021-05-26 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('filtered_image', models.ImageField(upload_to='')),
                ('content', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]