from django.contrib import admin

from . import models

admin.site.register(models.Doctor)
admin.site.register(models.Nurse)
admin.site.register(models.Patient)
admin.site.register(models.Hospital)
admin.site.register(models.MedicalRecord)


