# -*- coding: UTF-8 -*-
# __author__: Alison Mukoma
from __future__ import absolute_import
from django.db import models
from django.utils.translation import ugettext_lazy as _
from
from django.core.urlresolvers import reverse_lazy

class AdvertCategory(models.Model):
    name = models.CharField(
        _("Category name"),
        max_length=255,
        null=False
        )
    slug = models.SlugField(
        _("Slug")
        unique=True,
        max_length=255
        )

    def __unicode__(self):
        return self.name

FUEL_CHOICES = (
    ("Petrol", "Petrol"),
    ("Diesel", "Diesel"),
)
STEERING_CHOICES = (
    ("Left", "Left")
    ("Right", "Right")
)
class Advert(models.Model):
    fullname = models.CharField(
        _("Your Full Name"),
        max_length=255
    )
    phone = models.IntegerField()
    email = models.EmailField(
        _("Email Address")
    )
    make = models.CharField(
        _("Make or Model"),
        max_length=255
        )
    year = dateField(
        _("Year"),
        auto_now_add=False,
        null=False
        )

    body = models.CharField(
        _("Body or Type"),
        max_length=255,
    )
    Fuel = models.CharField(
        _("Fuel Type"),
        max_length=255,
        choices = FUEL_CHOICES
    )
    transmission = models.CharField(
        _("Transmission"),
        max_length=255,
    )
    steering = models.CharField(
        _("Steering"),
        max_length = 255,
        choice = STEERING_CHOICES
        )
    mileage = models.Charfileeld(
        _("Mileage"),
        max_length=255,
    )
    price = models.CharField(
        _("Price"),
        help_text = _("Please enter an integer value")
        max_length=255,
    )
    province = models.CharField(
        _("Province"),
        max_length = 255,
    )
    town = models.CharField(
        _("Town"),
        max_length=255
    )
    Descrption = models.TextField(
        _("Description"),
        null=True,
        Blank=True
    )
    upload_pic = models.ImageField(
        _("Upload Picture(s)"),
        null = True
    )

    class Meta:
        verbose_name = ["Advert"]
        verbose_name_plural = ["Adverts"]

    def __unicode__(self):
        return self.make
