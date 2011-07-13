from datetime import datetime, timedelta

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import TestCase

from polls.models import Choice, Poll
from polls.tests.utils import BaseTestCase

class TestPollSample(BaseTestCase):
    
    def setUp(self):
        super(TestPollSample,self).setUp()
        self.poll = Poll(
            question="What is your favorite number?",
            pub_date=datetime.now()
        )
        self.poll.save()
        for i in range(1, 4):
            choice = Choice(
                poll = self.poll,
                choice=str(i),
                votes=0
            )
            choice.save()        
    
    
    def test_poll_index(self):
        """ Check if the poll index displays """        
        
        # Now display me a poll!
        url = reverse("poll_index")
        response = self.client.get(url)
        
        # Show them the print!
        #print response
        
        self.assertContains(response, "What is your favorite number?")
        
    def test_poll_detail(self):
        """ Check if the poll detail displays """
        
        # Grab poll again to make sure we get right ID and that
        #   any custom save methods have been fully fired
        poll = Poll.objects.get(id=self.poll.id)
        
        url = reverse("poll_detail", kwargs={"poll_id": poll.id})
        response = self.client.get(url)
        
        self.assertContains(response, "What is your favorite number?")        
        
    def test_poll_vote(self):
        """ vote on a poll """
        url = reverse("poll_vote", kwargs={"poll_id": self.poll.id})
        
        # Pick a bad choice out of range
        data = dict(choice = 10)
        response = self.client.post(url, data, follow=True)
        self.assertContains(response, "You didn&#39;t select a choice.")
        
        # pick a choice in range
        data = dict(choice = 2)
        response = self.client.post(url, data, follow=True)
        self.assertContains(response, "<li>2 -- 1 vote</li>")
        