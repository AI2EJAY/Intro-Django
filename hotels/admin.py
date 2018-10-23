from django.contrib import admin
from .models import Apartment

class ApartmentAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')
# Register your models here.
admin.site.register(Apartment, ApartmentAdmin)



