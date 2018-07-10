from django.contrib import admin
from .models import Appointment, PersonalAppointment

admin.site.register((Appointment, PersonalAppointment))
