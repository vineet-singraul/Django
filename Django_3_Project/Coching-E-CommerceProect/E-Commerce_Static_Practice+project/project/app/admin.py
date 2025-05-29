from django.contrib import admin
from .models import Customer,Query,DynamicCards
# Register your models here.

admin.site.register(Customer)
admin.site.register(Query)
admin.site.register(DynamicCards)