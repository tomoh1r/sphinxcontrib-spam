# -*- coding: utf-8 -*-
u'''
    spam.sphinx_ext
    ~~~~~~~~~~~~~~~~~~~~

    Allow blockdiag-formatted diagrams to be included in Sphinx-generated
    documents inline.

    :copyright: Copyright by Tomohiro Nakamura.
    :license: New BSD License.
'''
from sphinx.util.compat import Directive, make_admonition
from docutils import nodes

SPAM = 'spam!'
SPAMS = 'spam! spam! spam!'


def spam_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    u'''chang str to "spam! spam! spam!".

    Returns 2 part tuple containing list of nodes to insert into the
    document and a list of system messages.  Both are allowed to be
    empty.

    :param name: The role name used in the document.
    :param rawtext: The entire markup snippet, with role.
    :param text: The text marked with the role.
    :param lineno: The line number where rawtext appears in the input.
    :param inliner: The inliner instance that called us.
    :param options: Directive options for customization.
    :param content: The directive content for customization.
    '''
    node = nodes.Text(' '.join([SPAM, text, SPAM]), rawtext)
    return [node], []


class SpamDirective(Directive):
    u'''Spamディレクティブ
    '''

    # この変数をセットすると、ディレクティブの中に
    # コンテンツを書けるようになります。
    has_content = True

    def run(self):
        env = self.state.document.settings.env

        ad = make_admonition(spam, self.name, [SPAM], self.options,
                             self.content, self.lineno, self.content_offset,
                             self.block_text, self.state, self.state_machine)

        spams = getattr(env, 'spam_all_spams', [])
        spams.append({
            'docname': env.docname,
            'lineno': self.lineno,
            'spam': ad[0].deepcopy(),
        })
        print(spams)
        env.spam_all_spams = spams

        return ad


def write_spam(app, doctree, fromdocname):
    '''
    env = app.builder.env
    for spam_info in env.spam_all_spams:
        para = nodes.paragraph()
        filename = env.doc2path(spam_info['docname'], base=None)
        description = \
                '(The original entry is located in %s, line %d and can be found ' \
                % (filename, spam_info['lineno'])
        para += nodes.Text(description, description)
        para += nodes.reference('', '')
        para += nodes.Text(SPAM)
        para += nodes.Text('.)', '.)')
    '''
    pass


def setup(app):
    u'''setup

    see http://sphinx.shibu.jp/ext/tutorial.html
    '''
    app.add_role('spam', spam_role)
    app.add_directive('spam', SpamDirective)
    app.connect("doctree-resolved", write_spam)
