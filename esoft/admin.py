from django.contrib import admin

from . import models


admin.site.register(models.Client)
admin.site.register(models.Agent)
admin.site.register(models.ObjectType)
admin.site.register(models.Object)
admin.site.register(models.District)
admin.site.register(models.Offer)
admin.site.register(models.Demand)
admin.site.register(models.Deal)