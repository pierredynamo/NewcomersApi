from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ClientsViewSet, CountriesViewSet, ClientsTypesViewSet, ServicesViewSet, AppointmentsViewSet

router = routers.DefaultRouter()
router.register('countries', CountriesViewSet)
router.register('clientstypes', ClientsTypesViewSet)
router.register('clients', ClientsViewSet)
router.register('services', ServicesViewSet)
router.register('appointments', AppointmentsViewSet)




urlpatterns = [
    path("", include(router.urls)),
]