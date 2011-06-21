from datetime import datetime, timedelta

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import TestCase

from polls.models import Choice, Poll
from polls.tests.utils import BaseTestCase

class TestPollSample(BaseTestCase):
    
    
    def test_poll_index(self):
        """ Check if the poll index displays """        
        
        # create me a poll
        poll = Poll(
            question="Why is Python awesome?",
            pub_date=datetime.now()
        )
        poll.save()
        
        # Now display me a poll!
        url = reverse("poll_index")
        response = self.client.get(url)
        
        # Show them the print!
        #print response
        
        self.assertContains(response, "Why is Python awesome?")
        
    def test_poll_detail(self):
        """ Check if the poll detail displays """
        # create me a poll
        new_poll = Poll(
            question="Why is Python teh awesome?",
            pub_date=datetime.now()
        )
        new_poll.save()
        
        # Grab poll again to make sure we get right ID and that
        #   any custom save methods have been fully fired
        poll = Poll.objects.get(id=new_poll.id)
        
        url = reverse("poll_detail", kwargs={"poll_id": poll.id})
        response = self.client.get(url)
        
        self.assertContains(response, "Why is Python teh awesome?")        
        