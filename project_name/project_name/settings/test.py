from base import *

# DO TEST COVERAGE
######### DEBUG
DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = DEBUG

INSTALLED_APPS += ('django_coverage', )

TEST_RUNNER = 'testrunner.OurCoverageRunner'
COVERAGE_MODULE_EXCLUDES = (
    'tests$', 'settings$', 'urls$', 'locale$',
    'migrations', 'fixtures', 'debug_toolbar',
    'admin',
)
COVERAGE_MODULE_EXCLUDES += BASE_APPS
COVERAGE_REPORT_HTML_OUTPUT_DIR = "coverage"

########## DATABASES
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}
