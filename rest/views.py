from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

class AddPost(PermissionRequiredMixin, CreateView):
    permission_required = ('rest.add_post', )