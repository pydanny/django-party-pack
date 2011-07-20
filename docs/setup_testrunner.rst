=========================
Setting up a test runner
=========================

Ned Batchelder's coverage.py is an invaluable tool for any Python project. django_coverage makes coverage.py run inside of Django, and this is my preferred way of using that tool.

Step 1 - environment prep
=========================

In your requirements.txt file, make sure you have the following::

    django-coverage==1.2
    coverage==3.4

In your virtualenv install the necessary requirements::

    $ pip install -r requirements.txt

Make a `coverage` directory in your project directory::

    $ mkdir coverage

Step 2 - create testrunner.py
=============================

Create a testrunner.py file into your project root and paste in the following code::

    # Make our own testrunner that by default only tests our own apps

    from django.conf import settings
    from django.test.simple import DjangoTestSuiteRunner
    from django_coverage.coverage_runner import CoverageRunner

    class OurTestRunner(DjangoTestSuiteRunner):
        def build_suite(self, test_labels, *args, **kwargs):
            return super(OurTestRunner, self).build_suite(test_labels or settings.PROJECT_APPS, *args, **kwargs)

    class OurCoverageRunner(OurTestRunner, CoverageRunner):
        pass

Step 3 - settings customization
===============================

The first thing you'll notice about dpp is that apps installment is broken up into three variables:

 * `PREREQ_APPS` - These are either built-in Django apps or third-party apps you don't want to test.
 * `PROJECT_APPS` - These are the custom apps you've written for your project. You want to test these.
 * `INSTALLED_APPS` - This is what Django loads into it's app cache. We generate this iterable by adding `PREREQ_APPS` to `PROJECT_APPS`.
 
Here is the sample code from dpp/pollaxe project settings.py file::
 
    PREREQ_APPS = (
         'django.contrib.auth',
         'django.contrib.contenttypes',
         'django.contrib.sessions',
         'django.contrib.sites',
         'django.contrib.messages',
         'django.contrib.admin',
    )

    PROJECT_APPS = (
        'polls', # or whatever your custom project uses
    )

    INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS 

Also in settings.py, underneath where you have defined the `PREREQ_APPS` setting, add the following::

    TEST_RUNNER = 'testrunner.OurCoverageRunner'
    COVERAGE_MODULE_EXCLUDES = [
        'tests$', 'settings$', 'urls$', 'locale$',
        'migrations', 'fixtures', 'admin$',
    ]
    COVERAGE_MODULE_EXCLUDES += PREREQ_APPS
    COVERAGE_REPORT_HTML_OUTPUT_DIR = "coverage"

Step 4 - run it!
================

From the command-line::

    $ python manage.py test

Open file:///path-to-your-project/coverage/index.html in a web browser and check out your coverage.