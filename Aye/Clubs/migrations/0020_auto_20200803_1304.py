# Generated by Django 3.0.5 on 2020-08-03 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clubs', '0019_auto_20200803_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='club_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clubs.clubs'),
        ),
    ]
