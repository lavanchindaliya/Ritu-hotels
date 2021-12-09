# Generated by Django 3.0.5 on 2020-09-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beerbar', '0017_auto_20200923_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('people', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('category', models.CharField(default='club', max_length=50)),
                ('image', models.ImageField(default='Images/None/No0img.jpg', upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='whisky',
        ),
    ]