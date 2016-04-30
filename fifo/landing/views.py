from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..queues.models import Queue
from ..entries.models import Entry

def home(request):
    context = {}
    
    
    active_queues = Queue.objects.filter(active=True)
    
    all_entries = []
    
    for queue in active_queues:
        entries = Entry.objects.filter(queue=queue, active=True)
        all_entries.append(entries)
        
    
    
    context['active_queues'] = zip(active_queues, all_entries)
    
    return render(request, 'landing/home.html', context)