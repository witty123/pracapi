from django.contrib import admin
from papi.models import Doctors, Clinics, DiagnosticLabs, Tests

admin.site.register(Doctors)
admin.site.register(Clinics)
admin.site.register(DiagnosticLabs)
admin.site.register(Tests)