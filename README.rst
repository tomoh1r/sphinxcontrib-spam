==================
sphinxcontrib-spam
==================

Features
========
This package contains the spam Sphinx extension.
This extension enable you to eat SPAM.

This module is under development for a while.

Set up
======
Make environment with easy_install::

    $ easy_install sphinxcontrib-spam

Convert Usage
=============
setup conf.py with::

   extensions = ['sphinxcontrib.spam']

if you use the spam role::

   :spam:`hoge`

and run::

   $ make html

Requirement
===========
- Python 2.4 or later (not support 3.x)
- Sphinx 1.0.x or later.

2. License
==========
Licensed under the `New BSD License <http://www.freebsd.org/copyright/freebsd-license.html>`_ .
See the LICENSE file for specific terms.
