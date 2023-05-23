from django.contrib import admin
from .models import Trade, Trader

# Register your models here.
admin.site.register(Trader)
admin.site.register(Trade)