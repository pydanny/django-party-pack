# Make our own testrunner that by default only tests our own apps

from django.conf import settings
from django.test.simple import DjangoTestSuiteRunner
from django_coverage.coverage_runner import CoverageRunner

# TODO write something that generates a coverage folder if it doesn't already exist

class OurTestRunner(DjangoTestSuiteRunner):
    def build_suite(self, test_labels, *args, **kwargs):
        return super(OurTestRunner, self).build_suite(test_labels or settings.PROJECT_APPS, *args, **kwargs)

class OurCoverageRunner(OurTestRunner, CoverageRunner):
    pass
