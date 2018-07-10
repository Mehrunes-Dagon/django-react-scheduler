from rest_framework import serializers, viewsets
from .models import Appointment, PersonalAppointment


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ('title', 'content')


class AppointmentViewset(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

# Personal Appointment


class PersonalAppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalAppointment
        fields = ('title', 'content')

    def create(self, validated_data):
        # import pdb
        # pdb.set_trace()
        user = self.context['request'].user
        personal_appointment = PersonalAppointment.objects.create(
            user=user, **validated_data)
        return personal_appointment


class PersonalAppointmentViewset(viewsets.ModelViewSet):
    serializer_class = PersonalAppointmentSerializer
    queryset = PersonalAppointment.objects.none()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return PersonalAppointment.objects.none()
        else:
            return PersonalAppointment.objects.filter(user=user)
