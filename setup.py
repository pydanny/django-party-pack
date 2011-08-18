from setuptools import setup, find_packages
import os
import shop

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
]

setup(
    author="#YOUR NAME HERE#",
    author_email="#YOU EMAIL HERE#",
    name='django-party-pack',

    version='0.0.1', # TODO: Make this rely on myapp.__version__ instead
    
    description='A Party pack for django!',

    # The following line uses README.rst as long description.
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),

    # Tip: do NOT use download-url! This makes it really painful for most
    # people using tools like buildout. Simply host your downloads on pypi, and
    # stop worrying.

    url='#A website URL here#',
    
    license='BSD License', # Obviously change it to something relevant
    platforms=['OS Independent'], # Python! Yay!
    
    classifiers=CLASSIFIERS,
    
    install_requires=open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).read(),

    packages=find_packages(), #This auto-finds and includes python pacakges!
    include_package_data=True,
    zip_safe = False,
)

