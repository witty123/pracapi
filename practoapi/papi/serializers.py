from rest_framework import serializers
from papi.models import Doctors, Clinics, DiagnosticLabs, Tests


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctors
        fields = ('doctor_id', 'name', 'gender', 'qualification', 'specialisation', 'availability', 'clinic')


class ClinicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clinics
        fields = ('clinic_id', 'name', 'address', 'phone')

class DiagnosticLabsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clinics
        fields = ('lab_id', 'name', 'address', 'phone')

class TestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clinics
        fields = ('test_id', 'name', 'description')