# Generated by Django 3.0.5 on 2020-08-08 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
