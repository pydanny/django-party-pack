==================
Coding Conventions
==================

So we are all on the same track.

Philosophy
~~~~~~~~~~

Zen of Python
=============

Try it out at the shell::

    import this

My favorite parts:

* Explicit is better than implicit.
* Simple is better than complex.
* Readability counts.
* Errors should never pass silently.

PEP-8 is my friend
==================

No `import *`! Even in `urls.py`!

All Docs go on rtfd.org!
========================

No alternative compares to http://rtfd.org. Not github, bitbucket, or google project wikis compare. And even the python.packages.com site is out of the lead of rtfd.org. Stop trying other things and come to the current leader in documentation hosting. Why?

1. It takes your repo and makes it look awesome.
2. It puts all the Python docs into one place for good searching.
3. It plays nice with git, hg, and svn.
4. Makes your project and work much more visible.
5. The lead maintainer, Eric Holscher, is incrediblysupportive and has both PSF and Revsys support. 

Code Bits
~~~~~~~~~~

Docs
====

Besides `admin.py`, all new python files need to be added to the appropriate `app_<app_name>.rst` or `reference_<app_name>.rst` file.

Templates
=========

* `snippets/_<name>.html` is for templates that are added via `include` or `templatetags`.
* ``{# unstyled #}`` is a flag for designers that the template is still untouched by their hands.

urls.py
=======

Even in urls.py you want clean code, right?

Explicit imports
----------------

See how it is done::

    # See this commented out? 'import *' usually slows things down AND makes it harder to debug
    # import *

    # Explicit imports are easier to debug
    from polls import views
    ...

Using the url() function
------------------------

Pythonistas love explicitly but this is implicit and henceforth not ideal::

    # Don't do this!
    url(
        r'^$',
        views.poll_list,
        'poll_list',
    ),
    
    # Or this!
    (
        r'^$',
        views.poll_list,
        'poll_list',
    ),

And here is the preferred and wonderfully explicit Jacob Kaplan-Moss / Frank Wiles pattern::

    url(
        regex=r'^$',
        view=views.poll_list,
        name='poll_list',
    ),
    

Calling specific views
----------------------

This is hard to debug because Django gets a bit too 'magical' and the trace often doesn't give you as much or is longer::

    # Don't do this!
    url(
        regex=r'^$',
        view='polls.views.standard.poll_list', # this single bit makes it harder to debug on errors
        name='poll_list',
    ),

Instead we do this::

    url(regex=r'^$',
        view=views.poll_list,
        name='poll_list',
    ),
    
Generic Exceptions are the DEVIL
---------------------------------

This is the DEVIL::

    try:
        do_blah()
    except:
        pass
        
Do this instead::

    class BlahDoesNotWork(Exception): pass

    try:
        do_blah
    except ImportError:
        # do something
    except AttributeError:
        # do something else
    except Exception as e:
        msg = "{0} has failed!".format(str(e))
        logging.error(msg)
        raise BlahDoesNotWork(msg)
