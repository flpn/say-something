from django.shortcuts import render
from django.views import generic 

from .models import Record


class IndexView(generic.ListView):
    template_name = 'records/index.html'

    def get_queryset(self):
        return Record.objects.all()
