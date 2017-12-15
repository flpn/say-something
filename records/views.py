from django.shortcuts import render
from django.views import generic 
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import Record


class IndexView(generic.ListView):
    template_name = 'records/index.html'

    def get_queryset(self):
        return Record.objects.order_by('-publication_date')[:5]


def submit(request):
    try:
        record_text = request.POST['record']
        
        if record_text == '':
            raise KeyError()

    except KeyError:
        record_list = Record.objects.order_by('-publication_date')[:5]
        context = { 
            'error_message': 'Write something before submit!',
            'record_list': record_list
        }
        
        return render(request, 'records/index.html', context)
    
    else:
        record = Record(text=record_text, publication_date=timezone.now())
        record.save()

        return HttpResponseRedirect(reverse('records:index'))
