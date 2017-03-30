# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 19:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pricetracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('shortName', models.TextField()),
                ('code', models.TextField()),
                ('symbol', models.TextField()),
                ('country', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PriceLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricetracker.Currency')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('url', models.URLField()),
                ('pubDate', models.DateTimeField(verbose_name='date published')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricetracker.WebStore')),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timing', models.DurationField()),
                ('lastCheck', models.DateTimeField()),
                ('pattern', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricetracker.Products')),
            ],
        ),
        migrations.AddField(
            model_name='pricelog',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricetracker.Products'),
        ),
    ]