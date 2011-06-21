from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from polls.models import Choice, Poll
from polls.tests.utils import BaseTestCase

class TestPolls(BaseTestCase):
    
    
    def test_poll_create(self):
        """ Can we create a poll?
        
        * Seems trivial now
        * But for complex systems what started out as a simple create can get complex
        * Get your test coverage up!
        """                
        
        poll_count = Poll.objects.count()
        poll = Poll(
            question="Why is Python awesome?",
            pub_date=datetime.now()
        )
        poll.save()
        self.assertTrue(poll_count < Poll.objects.count())