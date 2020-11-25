from django.contrib import admin

# Register your models here.
from .models import IPLSeason, Matches

# Register your models here.
admin.site.register(IPLSeason)
admin.site.register(Matches)