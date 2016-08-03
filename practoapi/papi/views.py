from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from papi.serializers import DoctorSerializer, ClinicSerializer, DiagnosticLabsSerializer, TestsSerializer
from papi.models import Doctors, Clinics, DiagnosticLabs, Tests


class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Doctors to be viewed or edited.
    """
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer


class ClinicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clinic to be viewed or edited.
    """
    queryset = Clinics.objects.all()
    serializer_class = ClinicSerializer

class DiagnosticLabsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Labs to be viewed or edited.
    """
    queryset = DiagnosticLabs.objects.all()
    serializer_class = DiagnosticLabsSerializer


class TestsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tests to be viewed or edited.
    """
    queryset = Tests.objects.all()
    serializer_class = TestsSerializer

