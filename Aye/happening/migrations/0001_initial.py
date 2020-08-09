# Generated by Django 3.0.5 on 2020-07-30 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Happening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=140)),
                ('photo', models.ImageField(default='', upload_to='happening_images')),
                ('time', models.TextField(max_length=50)),
                ('link', models.URLField(max_length=50)),
            ],
        ),
    ]
