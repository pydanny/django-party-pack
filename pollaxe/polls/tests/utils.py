from django.contrib.auth.models import User
from django.test import TestCase


class BaseTestCase(TestCase):

    urls = 'polls.urls'

    def setUp(self):
        """ Provides a self.user and self.user_pw

        usage::

            from polls.tests.utils import BaseTestCase
            class MyTest(BaseTestCase):

                def setUp(self):
                    super(MyTest,self).setUp()
                    # stick in custom setUp bits here
                    # stick in custom setUp bits here
                    # stick in custom setUp bits here
                """

        # I always forget the password
        self.user_pw = 'test'

        # Create a sample user
        self.user = User.objects.create_user('pydanny', 'pydanny@test.com', self.user_pw,)
        self.user.first_name = "Danny"
        self.user.last_name = "Greenfeld"
        self.user.save()

    def tearDown(self):
        self.client.logout()

    def login(self, user, password):
        return login(self, user, password)
