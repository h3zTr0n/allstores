# -*- coding: UTF-8 -*-
# __author__: Alison Mukoma

from __future__ import absolute_import
from django.contrib import admin

from .models import Advert
from .models import AdvertCategory

# Advert model admin registration
class AdvertModelAdmin(admin.ModelAdmin):
    list_display = ["make", "price"]
admin.site.register(Advert, AdvertModelAdmin)

# Advert category model admin registration
class AdvertCategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name"]
admin.site.register(AdvertCategory, AdvertCategoryModelAdmin)
