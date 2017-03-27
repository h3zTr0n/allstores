# -*- coding: UTF-8 -*-
# __author__: Alison Mukoma
from __future__ import absolute_import
from django.db import models
from django.utils.translation import ugettext_lazy as _
# from django.core.urlresolvers import reverse_lazy

class AdvertCategory(models.Model):
    name = models.CharField(
        _("Category name"),
        max_length=255,
        null=False
        )
    notes = models.CharField(
        _("Notes"),
        max_length = 255,
    )
    slug = models.SlugField(
        _("Slug"),
        # unique=True,
        max_length=255
        )
    class Meta:
        verbose_name = "Advert Category"
        verbose_name_plural = "Advert Categories"

    def __unicode__(self):
        return self.name

FUEL_CHOICES = (
    ("Petrol", "Petrol"),
    ("Diesel", "Diesel"),
)
STEERING_CHOICES = (
    ("Left", "Left"),
    ("Right", "Right"),
)

# Advert class(object)
class Advert(models.Model):
    category = models.ForeignKey(AdvertCategory)
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
    year = models.DateField(
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
        max_length=255
    )
    steering = models.CharField(
        _("Steering"),
        max_length = 255,
        choices = STEERING_CHOICES
        )
    mileage = models.CharField(
        _("Mileage"),
        max_length=255
    )
    price = models.CharField(
        _("Price"),
        help_text = _("Please enter an integer value"),
        max_length=255
    )
    province = models.CharField(
        _("Province"),
        max_length = 255
    )
    town = models.CharField(
        _("Town"),
        max_length=255
    )
    Descrption = models.TextField(
        _("Description"),
        null=True,
        blank=True
    )
    upload_pic = models.ImageField(
        _("Upload Picture(s)"),
        null = True
    )
    from django.utils import timezone
    created = models.DateTimeField(
        # auto_now=True,
        default=timezone.now
        )
    modified = models.DateTimeField(
        # auto_now_add=True
        default=timezone.now
        )
    # ad_id = models.IntegerField(
    #     _("advert ID")
    #     default
    # )
    status = models.BooleanField(
        _("Status"),
        default = False
    )
    notes = models.TextField(
        null=False,
        blank=False,
        default = "notes"
    )


    class Meta:
        verbose_name = "Advert"
        verbose_name_plural = "Adverts"

    def __unicode__(self):
        return self.make
