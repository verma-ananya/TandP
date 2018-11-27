# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.conf import settings

# Create your models here.


class CV_attr(models.Model):
	name = models.CharField(max_length = 30)
	email = models.CharField(max_length = 40)
	mobile = models.DecimalField(max_digits=10 , decimal_places=0)
	github = models.URLField(max_length=200)
	personal = models.CharField(max_length= 200)
	branch = models.CharField(max_length=3)
	proj_1_title = models.CharField(max_length=100)
	proj_1_date = models.CharField(max_length=30)
	proj_1_desc = models.CharField(max_length=200)
	proj_2_title = models.CharField(max_length=100)
	proj_2_date = models.CharField(max_length=30)
	proj_2_desc = models.CharField(max_length=200)
	proj_3_title = models.CharField(max_length=100)
	proj_3_date = models.CharField(max_length=30)
	proj_3_desc = models.CharField(max_length=200)	
	skill_1 = models.CharField(max_length=30)
	skill_2 = models.CharField(max_length=30)
	skill_3 = models.CharField(max_length=30)
	skill_4 = models.CharField(max_length=30)
	skill_5 = models.CharField(max_length=30)
	skill_6 = models.CharField(max_length=30)
	skill_7 = models.CharField(max_length=30)
	skill_8 = models.CharField(max_length=30)
	skill_9 = models.CharField(max_length=30)
	degree = models.CharField(max_length=100)
	College_name = models.CharField(max_length=100)
	college_cgpa = models.DecimalField(max_digits=4 , decimal_places=2)
	exam_12 = models.CharField(max_length=100)
	school_12_name = models.CharField(max_length=100)
	school_12_perc = models.DecimalField(max_digits=4 , decimal_places=2)
	exam_10 = models.CharField(max_length=100)
	school_10_name = models.CharField(max_length=100)
	school_10_perc = models.DecimalField(max_digits=4 , decimal_places=2)	

	def __str__(self):
		return self.name
