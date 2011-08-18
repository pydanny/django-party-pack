# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
import codecs

# The following classifiers are a good start, and a safe bet
# A list of classifiers can be found here:
# http://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
     'Development Status :: 2 - Pre-Alpha', # Change this accordingly
     'Environment :: Web Environment',
     'Framework :: Django',
     'Intended Audience :: Developers',
     'License :: OSI Approved :: BSD License',
     'Operating System :: OS Independent',
     'Programming Language :: Python',
     'Programming Language :: Python :: 2',
     'Programming Language :: Python :: 2.6', # Maybe add 2.7
]

setup(
    author="#YOUR NAME HERE#",
    author_email="#YOU EMAIL HERE#",
    name='django-party-pack',
    
    # The actual version string is defined in pollaxe/__init__.py
    version= __import__('pollaxe').__version__
    
    description='A Party pack for django!',

    # The following line uses README.rst as long description.
    long_description=codecs.open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'utf-8').read(),

    # Tip: do NOT use download-url! This makes it really painful for most
    # people using tools like buildout. Simply host your downloads on pypi, and
    # stop worrying.

    url='#A website URL here#',
    
    license='BSD License', # Obviously change it to something relevant
    platforms=['OS Independent'], # Python! Yay!
    
    classifiers=CLASSIFIERS,

    # This might seem like a repetition of requirements.txt, but this applies
    # to the *package*, and requirements are for the *environment*.
    install_requires=[
        'django==1.3',
        'sphinx=1.0.7',
        'django-coverage==1.2',
        'coverage==3.4',
    ],

    packages=find_packages(), #This auto-finds and includes python pacakges!
    include_package_data=True,
    zip_safe = False,
)

