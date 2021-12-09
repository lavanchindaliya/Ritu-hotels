# Generated by Django 3.0.5 on 2020-09-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beerbar', '0013_order_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('category', models.CharField(default='rum', max_length=50)),
                ('image', models.ImageField(default='Images/None/No0img.jpg', upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Vodka',
        ),
    ]