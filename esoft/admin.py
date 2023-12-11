from django.contrib import admin

from . import models


admin.site.register(models.Client)
admin.site.register(models.Agent)
admin.site.register(models.Types)
admin.site.register(models.Coordinate)
admin.site.register(models.Object)
admin.site.register(models.District)
admin.site.register(models.Offer)
admin.site.register(models.Need)
admin.site.register(models.Deal)