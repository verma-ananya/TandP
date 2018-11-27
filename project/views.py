# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Project
from .forms import ProjectForm
from django.shortcuts import redirect
# Create your views here.


def post_list(request):
	projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'student_after_login.html', {'projects': projects})


def post_new(request):
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_edit.html', pk=post.pk)
	else:
		form = ProjectForm()
	return render(request, 'post_edit.html', {'form': form})
