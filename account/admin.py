from django.contrib import admin

from account.models import CountryNames, PartnersDetails

# Register your models here.

admin.site.register(PartnersDetails)
admin.site.register(CountryNames)