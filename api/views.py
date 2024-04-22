from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Clients, ClientsTypes, Countries, Services, Appointments
from .serializers import (ClientsSerializer, ClientsTypesSerializer, CountriesSerializer, ServicesSerializer,
                          AppointmentsSerializer)
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication


class ClientsTypesViewSet(viewsets.ModelViewSet):
    queryset = ClientsTypes.objects.all()
    serializer_class = ClientsTypesSerializer
    authentication_classes = (TokenAuthentication,)

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    authentication_classes = (TokenAuthentication,)

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    authentication_classes = (TokenAuthentication,)



class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    authentication_classes = (TokenAuthentication,)
    @action(detail=True, methods=['POST'])
    def countries(self, request, pk=None):
        if 'country' in request.data:
            countr = Countries.objects.get(pk=pk)
            countrcd = request.data['country']
            user = request.user
            print('user', user.id)
            try:
                country = Countries.objects.get(user=user.id, country=countr.id)
                country.countrycode = countrcd
                country.country = country
                country.save()
                response = {'message' : 'it is working'}
                return Response(response, status=status.HTTP_200_OK)
            except:
                Countries.objects.create(user=user, country=countr)
        else:
            response = {'message' : 'you need to type all the fields'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class AppointmentsViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentsSerializer
    authentication_classes = (TokenAuthentication,)





# Create your views here.
