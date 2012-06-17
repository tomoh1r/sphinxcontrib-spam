# -*- coding: utf-8 -*-

from sphinxcontrib.spam import spam
from docutils.parsers.rst.states import Inliner


def test_pass():
    assert True


def test_spam_role():
    u'''ロールが指定された場合、正しいnodeが出力されること。
    '''
    ilr = Inliner()
    node = spam.spam_role('spam', u':spam:`あばばばば`',
            u'あばばばば', 123, ilr)[0][0]
    assert unicode(node) == u'spam! あばばばば spam!'
