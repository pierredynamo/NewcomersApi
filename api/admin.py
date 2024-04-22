from django.contrib import admin
from .models import Clients, ClientsTypes, Countries, Services, Appointments


# Register your models here.
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('fistname', 'name', 'email', 'address', 'phone', 'type',)

class ClientsTypesAdmin(admin.ModelAdmin):
    list_display = ('type',)

class CountriesAdmin(admin.ModelAdmin):
    list_display = ('contrycode', 'country',)

class ServivesAdmin(admin.ModelAdmin):
    list_display = ('service_name', )

class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'service_name', 'datetime',)

admin.site.register(Clients, ClientsAdmin)
admin.site.register(ClientsTypes, ClientsTypesAdmin)
admin.site.register(Countries, CountriesAdmin)
admin.site.register(Services, ServivesAdmin)
admin.site.register(Appointments, AppointmentsAdmin)