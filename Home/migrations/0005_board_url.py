# Generated by Django 3.0.7 on 2022-02-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20220201_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='url',
            field=models.URLField(default='https://swc.iitg.ac.in/stud/gymkhana'),
        ),
    ]