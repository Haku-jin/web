from __future__ import unicode_literals
from django.db import models


class WebStore(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.TextField()
    shortName = models.TextField()
    code = models.TextField()
    symbol = models.TextField()
    country = models.TextField()

    def __str__(self):
        return self.code


class Products(models.Model):
    name = models.TextField()
    url = models.URLField()
    store = models.ForeignKey(WebStore, on_delete=models.CASCADE)
    pubDate = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class Tracker(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    timing = models.DurationField()
    lastCheck = models.DateTimeField()
    pattern = models.TextField()


class PriceLog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
