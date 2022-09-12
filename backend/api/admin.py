from django.contrib import admin

from api.models import Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('bankname',)


admin.site.register(Offer, OfferAdmin)
