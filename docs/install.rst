=============
Installation
=============

.. note:: For things with `$ font like this` it means type it at the command line and hit enter.

Before you start
================

1. Make sure you have virtualenv installed. 
2. Make sure you have git-scm installed

Create a virtualenv for this project. We do this so we isolate all our work from the rest of Python on our computer::

    $ virtualenv dpkenv
    $ source dpkenv/bin/activate

The Basics
===========

First we clone django-party-pack and go into django-party-pack::

    $ git clone https://pydanny@github.com/pydanny/django-party-pack.git
    $ cd django-party-pack
    
Now let's install our dependencies::

    $ pip install -r requirements.txt
    
This may take a few minutes. Feel free to go get some coffee. :)

Building the sphinx docs
=========================

1. change directory to docs
2. **make html**

Running django-coverage
========================

1. python manage.py test