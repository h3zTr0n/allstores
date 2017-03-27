# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('fullname', models.CharField(verbose_name='Your Full Name', max_length=255)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(verbose_name='Email Address', max_length=254)),
                ('make', models.CharField(verbose_name='Make or Model', max_length=255)),
                ('year', models.DateField(verbose_name='Year')),
                ('body', models.CharField(verbose_name='Body or Type', max_length=255)),
                ('Fuel', models.CharField(verbose_name='Fuel Type', choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel')], max_length=255)),
                ('transmission', models.CharField(verbose_name='Transmission', max_length=255)),
                ('steering', models.CharField(verbose_name='Steering', choices=[('Left', 'Left'), ('Right', 'Right')], max_length=255)),
                ('mileage', models.CharField(verbose_name='Mileage', max_length=255)),
                ('price', models.CharField(verbose_name='Price', help_text='Please enter an integer value', max_length=255)),
                ('province', models.CharField(verbose_name='Province', max_length=255)),
                ('town', models.CharField(verbose_name='Town', max_length=255)),
                ('Descrption', models.TextField(verbose_name='Description', null=True, blank=True)),
                ('upload_pic', models.ImageField(verbose_name='Upload Picture(s)', null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Advert',
                'verbose_name_plural': 'Adverts',
            },
        ),
        migrations.CreateModel(
            name='AdvertCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Category name', max_length=255)),
                ('slug', models.SlugField(verbose_name='Slug', max_length=255)),
            ],
            options={
                'verbose_name': 'Advert Category',
                'verbose_name_plural': 'Advert Categories',
            },
        ),
        migrations.AddField(
            model_name='advert',
            name='category',
            field=models.ForeignKey(to='advertisment.AdvertCategory'),
        ),
    ]
