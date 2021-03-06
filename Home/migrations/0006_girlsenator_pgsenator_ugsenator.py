# Generated by Django 3.2.4 on 2021-12-24 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_senator_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='GirlSenator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=20)),
                ('linked_in', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PGSenator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=20)),
                ('linked_in', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UGSenator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=20)),
                ('linked_in', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
    ]
