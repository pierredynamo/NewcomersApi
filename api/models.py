from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Services(models.Model):
    """
        Request : Accommodation, School settlement, Community development
    """
    service_name = models.CharField(max_length=150, unique=True, primary_key=True, verbose_name='Purpose of the Appointment')
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    def __str__(self):
        return self.service_name
class ClientsTypes(models.Model):
    """
        Types of Clients : Permanent Resident, Temporary resident, Canadian Citizen, visitor, or refugee
    """
    type = models.CharField(max_length=50, primary_key=True, unique=True, verbose_name='Residency status')
    class Meta:
        verbose_name = 'Residency status'
        verbose_name_plural = 'Residency status'

    def __str__(self):
        return self.type

class Countries(models.Model):
    country = models.CharField(max_length=50, primary_key=True, unique=True, null=False, blank=False, verbose_name="Country")
    contrycode = models.CharField(max_length=3, null=False, blank=False)
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
    def __str__(self):
        return self.country
class Clients(models.Model):
    """
        New comers in Canada that need the support of FRAP
    """
    name = models.CharField(max_length=70, null=False, blank=False, verbose_name="Name")
    mname = models.CharField(max_length=70, null=True, blank=True, verbose_name="Middle name")
    fistname = models.CharField(max_length=100, null=True, blank=True, verbose_name="First name")
    dob = models.DateField(null=False, blank=False,verbose_name="Date of birth")
    countryb = models.ForeignKey(Countries,on_delete=models.CASCADE, verbose_name="Country of birth")
    email = models.EmailField(null=False, blank=False,verbose_name="Email")
    phone = models.CharField(max_length=20, null=False, blank=False, verbose_name="Phone number")
    address = models.CharField(max_length= 100, null=False, blank=False, verbose_name="Address")
    dol = models.DateField(null=False, blank=False, verbose_name="Date of arrival")
    dRP = models.DateField(null=True, blank=True, verbose_name="Date of PR")
    type = models.ForeignKey(ClientsTypes, on_delete=models.CASCADE, verbose_name="Residency status")
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    def __str__(self):
        return self.fistname + " " + self.mname+ " " + self.name

class Appointments(models.Model):
    """
        List of Appointment : Accommodation, School settlement, Community development
    """
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name="Client Name")
    service_name = models.ForeignKey(Services, on_delete=models.PROTECT, verbose_name="Purpose of the Appointment")
    datetime = models.DateTimeField(null=False, blank=False, verbose_name="Time of Appointment")

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'



from django.db import models

# Create your models here.
