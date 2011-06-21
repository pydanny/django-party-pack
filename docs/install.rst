=============
Installation
=============

.. note:: For things with **font like this** it means type it at the command line and hit enter.

The Basics
===========

0. **git clone https://pydanny@github.com/pydanny/sphinxified-django.git**
1. Make sure you have virtualenv installed.
2. change directory to the directory that contains this README.rst file.
3. **virtualenv pollaxe** and then **source pollaxe/bin/activate**
4. **pip install -r requirements.txt**
5. **mkdir pollaxe/coverage**

Building the sphinx docs
=========================

1. change directory to docs
2. **make html**

Running django-coverage
========================

1. python manage.py test