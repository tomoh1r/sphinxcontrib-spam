# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from sphinxcontrib import spam


def test_SpamDirective():
    spam_ = spam.SpamDirective()
    assert isinstance(spam_, spam.SpamDirective)
