# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def home(request):
	return render(request, 'home1.html')


def student_after_login(request):
	return render(request, 'student_after_login.html')

def projects(request):
	return render(request, 'projects.html')


def industry_committee(request):
	return render(request, 'industry_committee.html')


def contact(request):
	return render(request, 'contact_tp.html')
