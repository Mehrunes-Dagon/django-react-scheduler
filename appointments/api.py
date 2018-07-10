from rest_framework import serializers, viewsets
from .models import Appointment


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ('title')


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
