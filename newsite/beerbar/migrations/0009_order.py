# Generated by Django 3.0.5 on 2020-07-18 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beerbar', '0008_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('price', models.CharField(max_length=70)),
            ],
        ),
    ]
