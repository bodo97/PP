from django.contrib import admin
from .models import PatientData,PatientMob,PatientAdd
from .models import DoctorData,DoctorSpec,DoctorAppointment
from .models import PatientAppointmentsBooked



class ShowInfo(admin.ModelAdmin):
	list_display=["full_name","email","gender"]
class ShowMob(admin.ModelAdmin)	:
	list_display=["email","phone_number"]
class ShowAdd(admin.ModelAdmin):
	list_display=["email","City"]

class ShowDInfo(admin.ModelAdmin):
	list_display=["doc_id","doc_name"]

class ShowDspec(admin.ModelAdmin):
	list_display=["doc_id","doc_spec"]

class ShowDAppo(admin.ModelAdmin):
	list_display=["doc_id","PatientName","appointmentdate","status"]

class showAppoint(admin.ModelAdmin)	:
	list_display=["PatientName","email","doc_id","status"]

admin.site.register(PatientData,ShowInfo)
admin.site.register(PatientMob,ShowMob)
admin.site.register(PatientAdd,ShowAdd)

admin.site.register(DoctorData,ShowDInfo)
admin.site.register(DoctorSpec,ShowDspec)
admin.site.register(DoctorAppointment,ShowDAppo)
admin.site.register(PatientAppointmentsBooked,showAppoint)
# Register your models here.
