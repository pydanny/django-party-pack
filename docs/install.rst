=============
Installation
=============

.. note:: For things with the following it means type it at the command line and hit enter::

    $ ls -al

Before you start
================

Make sure you have virtualenv installed::

    $ which virtualenv
    /usr/local/bin/virtualenv 
    # You should get a response. This is mine but yours may vary. 
    #   No response means you need to install it.
    
If you need to install virtualenv::

    # TODO - find a good install link

Make sure you have git-scm installed::

    # TODO - find a good install link

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

Settings things
===============

TODO - add stuff so that new settings format works


Building the sphinx docs
=========================

First we need to change to our docs directory::

    $ cd docs
    
Now we generate the sphinx docs in html format::

    $ make html
    

2. **make html**

Running django-coverage
========================

1. python manage.py test