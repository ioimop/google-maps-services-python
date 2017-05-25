import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.version_info <= (2, 4):
    error = 'Requires Python Version 2.5 or above... exiting.'
    print >> sys.stderr, error
    sys.exit(1)


requirements = [
    'aiohttp >= 2.0.7',
]

setup(name='aiogmaps',
      version='2.4.6-dev',
      description='Python client library for Google Maps API Web Services',
      scripts=[],
      url='https://github.com/ioimop/google-maps-services-python',
      packages=['aiogmaps'],
      license='Apache 2.0',
      platforms='Posix; MacOS X; Windows',
      setup_requires=requirements,
      install_requires=requirements,
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Apache Software License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Internet',
                   ]
      )
