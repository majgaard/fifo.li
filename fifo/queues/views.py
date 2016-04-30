from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Queue
from ..entries.models import Entry

@login_required
def active_queues(request):
    context = {}
    
    return render(request, 'queues/active_queues.html', context)

@login_required
def all_queues(request):
    context = {}
    queues = Queue.objects.filter(owner=request.user.id)
    context['queues'] = queues
    
    return render(request, 'queues/all_queues.html', context)

@login_required
def queue_detail(request, id):
    context = {}
    
    return render(request, 'queues/queue_detail.html', context)

@login_required
def manage_queue(request, id):
    context = {}
    
    queue = Queue.objects.get(id=id)
    entries = Entry.objects.filter(queue=queue, active=True)
    
    context['queue'] = queue
    context['entries'] = entries
   
    
    return render(request, 'queues/manage_queue.html', context)