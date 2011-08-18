=============
Installation
=============

.. note:: For things with the following it means type it at the command line and hit enter::

    $ ls -al

Before you start
================

Do you have pip, virtualenv, virtualenvwrapper, and git-scm installed? If not, you'll need to get those on your machine before proceeding.

If you need to install pip::

    $ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
    $ python get-pip.py
    
If you need to install virtualenv:

    * http://virtualenv.org
    
If you need to install virtualenvwrapper:

    * http://www.doughellmann.com/docs/virtualenvwrapper/install.html

If you need to install git:

    * http://git-scm.com

The Basics
===========

Create a virtualenv for this project. We do this so we isolate all our work from the rest of Python on our computer::

    $ mkvirtualenv dpkenv

Now we clone django-party-pack and go into django-party-pack::

    $ git clone https://pydanny@github.com/pydanny/django-party-pack.git
    $ cd django-party-pack
    
Now let's install our dependencies::

    $ pip install -r requirements.txt
    
This may take a few minutes. Feel free to go get some coffee. :)

Settings setup
===============

We're going to follow what Django BDFL Jacob Kaplan-Moss `advocates as best practices for dealing with settings`_. That means we're going to ignore the manage.py file in the root of our Django project and use the django-admin.py script. In order to do that, we need to take a few more steps.

First, we add some virtualenv bits to allow us to access the settings properly::

    $ echo "export DJANGO_SETTINGS_MODULE=settings.local" >> $VIRTUAL_ENV/bin/postactivate
    $ echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate
    
This will allow you to eschew passing in --settings= into management commands.

Now we add to the virtualenv paths our pollaxe project::

    add2virtualenv <<path to django-party-pack repo>>/pollaxe

Running standard Django Commands
================================

Try out the project::

    $ django-admin.py syncdb
    $ django-admin.py runserver

Running django-coverage
========================

Simple run this command::

    $ django-admin.py test

Now open the pollaxe/coverage/index.html file in your favorite browser.

    
Building these sphinx docs
==========================

Want to have a local copy of these documents? Easy! Change to our docs directory::

    $ cd docs

Now we generate the sphinx docs in html format::

    $ make html

.. _`advocates as best practices for dealing with settings`: http://www.slideshare.net/jacobian/the-best-and-worst-of-django/51