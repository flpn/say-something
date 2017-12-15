from django.shortcuts import render
from django.views import generic 
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Record


class IndexView(generic.ListView):
    template_name = 'records/index.html'

    def get_queryset(self):
        return Record.objects.order_by('publication_date')[:5]


def submit(request):
    return HttpResponseRedirect(reverse('records:index'))
