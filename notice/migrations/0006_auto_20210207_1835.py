# Generated by Django 3.1.5 on 2021-02-07 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0005_auto_20210207_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(upload_to='userimage/%Y/%m/%d/'),
        ),
    ]
