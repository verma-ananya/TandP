from django.shortcuts import render
from django.db import models
from cvbuilder.models import CV_attr
# Create your views here.


def build_cv(request):
	cred = CV_attr.objects.get(id=1)
	return render(request, 'cv_builder.html', {'cred': cred})
