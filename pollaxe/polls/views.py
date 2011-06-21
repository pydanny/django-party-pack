from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader

from polls.models import Poll, Choice

def poll_index(request, template_name="polls/index.html"):
    """ Show a list of polls"""
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response(template_name, {'latest_poll_list': latest_poll_list})
    


def poll_detail(request, poll_id, template_name="polls/detail.html"):
    """ Show detail on a poll"""    
    poll = get_object_or_404(Poll, pk=poll_id)
    choices = Choice.objects.filter(Choice, poll=poll)
    return render_to_response(template_name, {'poll': poll, 'choices': choices})    
