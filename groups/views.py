from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)

from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
# Create your views here.
from groups.models import Group, GroupMember

class CreateGroup(LoginRequiredMixin, CreateView):
	fields =('name', 'description')
	model = Group

class SingleGroup(DetailView):
	model = Group

class ListGroups(ListView):
	model = Group