#!/usr/bin/env python

from distutils.core import setup

setup(name='kata',
      version='1.0',
      description='Exercises',
      author='Brandon T. Fields',
      author_email='brandon@cdated.com',
      url='http://www.cdated.com',
      packages=['kata'],
      entry_points = {
          'console_scripts': ['kata-quote=kata.main:main'],
      },
     )
