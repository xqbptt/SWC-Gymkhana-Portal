# Generated by Django 3.2.4 on 2022-01-03 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_auto_20220103_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='tag',
            field=models.IntegerField(null=True),
        ),
    ]
