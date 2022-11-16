from django.contrib import admin
# Primero importamos
from .models import Service

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# Llamamos al modelo que creamos
admin.site.register(Service, ServiceAdmin)
