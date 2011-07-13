from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader, RequestContext

from polls.models import Poll, Choice

POLL_DETAIL_TEMPLATE = "polls/detail.html"

# We pass the template_name as a variable because it makes the template function easier to 
# identify AND because it means it can be changed on the fly
def index(request, template_name="polls/index.html"):
    """ Show a list of polls"""
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response(template_name, {'latest_poll_list': latest_poll_list})


def detail(request, poll_id, template_name=POLL_DETAIL_TEMPLATE):
    """ Show detail on a poll"""    
    
    # I used 'poll' instead of 'p' because the pixel shortage is over.
    # If this is too much typing, then just cut-and-paste, okay?
    poll = get_object_or_404(Poll, pk=poll_id)
    choices = Choice.objects.filter(poll=poll)
    return render_to_response(template_name, {
        'poll': poll,
        'choices': choices }, 
        context_instance=RequestContext(request))    

def vote(request, poll_id, template_name=POLL_DETAIL_TEMPLATE):
    """ user votes on a poll"""

    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response(template_name, {
            'poll': poll,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        url = reverse('poll_results', args=(p.id,))
        return HttpResponseRedirect(url)    