# Generated by Django 3.0.5 on 2020-09-23 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beerbar', '0014_auto_20200922_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(default='room', max_length=50),
        ),
    ]