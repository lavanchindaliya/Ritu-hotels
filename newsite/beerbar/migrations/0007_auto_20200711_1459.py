# Generated by Django 3.0.5 on 2020-07-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beerbar', '0006_rum_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('image', models.ImageField(default='Images/None/No0img.jpg', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Mezcal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('image', models.ImageField(default='Images/None/No0img.jpg', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Vodka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('image', models.ImageField(default='Images/None/No0img.jpg', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('image', models.ImageField(default='Images/None/No0img.jpg', upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='beer',
            name='category',
        ),
        migrations.RemoveField(
            model_name='rum',
            name='category',
        ),
        migrations.RemoveField(
            model_name='whisky',
            name='category',
        ),
    ]
