from __future__ import unicode_literals
from django.db import models
import datetime
from .validators import valid_mob
# Create your models here.
'''

	Here the models for the table for the patient is created

'''
class PatientData(models.Model):
	Gender_choices=(
		('M','Male'),
		('F','Female'),
		)
	email			= models.EmailField(unique=True)
	full_name 		= models.CharField(max_length=100,blank=False,null=False)
	date_of_birth	= models.DateField(null=False,blank=False)
	gender			= models.CharField(max_length=1,choices=Gender_choices)
	# patientid		= models.CharField(max_length=)
	def age(self):
		return int((datetime.date.today() - self.birthday).days / 365.25  )

	def __str__(self):
		return str(self.email)

	def __unicode__(self):
		return str(self.email)
    # def __str__(self):

    # 	return str(self.full_name)
class PatientMob(models.Model):
	email 			= models.ForeignKey(PatientData)
	phone_number    = models.CharField(max_length=10,validators=[valid_mob], blank=False)

	def __str__(self):
		return str(self.email)

class PatientAdd(models.Model):
	email 			= models.ForeignKey(PatientData)
	house_num		= models.IntegerField(blank=False)
	Locality		= models.CharField(max_length=100,blank=False)
	City			= models.CharField(max_length= 15,blank=False)

	def __str__(self):
		return str(self.email)

'''
	Here the model for the table for the doctor table is created

'''
class DoctorData(models.Model):
	doc_id			= models.IntegerField(blank=False,unique=True)
	doc_name		= models.CharField(max_length=100,blank=False)
	doc_mobile		= models.CharField(max_length=10,validators=[valid_mob],blank=False)
	def __str__(self):
		return str(self.doc_id)

class DoctorSpec(models.Model):
	doc_id			= models.ForeignKey(DoctorData)
	doc_spec		= models.CharField(max_length=20,blank=False)
	def __str__(self):
		return str(self.doc_id)

class DoctorAppointment(models.Model):
	doc_id			= models.ForeignKey(DoctorData)
	email 			= models.ForeignKey(PatientData)
	appointmentdate = models.DateField(null=False,blank=False)
	status			= models.BooleanField(default=True)
	def PatientName(self):
		return self.email.full_name
			
	def __str__(self):
		return str(self.doc_id)

'''
	Now relation between patient and dcotor
'''
class PatientAppointmentsBooked(models.Model):
	doc_id			= models.ForeignKey(DoctorData)
	email 			= models.ForeignKey(PatientData)
	appointmentdate = models.DateField(null=False,blank=False)
	status			= models.BooleanField(default=True)

	def PatientName(self):
		return self.email.full_name


	def __str__(self):
		return str(self.email)
