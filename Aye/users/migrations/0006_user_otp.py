# Generated by Django 3.0.5 on 2020-08-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200727_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(default='', max_length=10),
        ),
    ]
