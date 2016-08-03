from __future__ import unicode_literals

from django.db import models

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Doctors (models.Model):
	doctor_id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=200)
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	qualification = models.TextField()
	specialisation = models.TextField()
	availability = models.CharField(max_length=200)
	clinic = models.ManyToManyField('Clinics')

class Clinics(models.Model):
	clinic_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	address = models.TextField()
	phone = models.IntegerField()

class DiagnosticLabs(models.Model):
	lab_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	address = models.TextField()
	phone = models.IntegerField()

class Tests(models.Model):
    test_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)

