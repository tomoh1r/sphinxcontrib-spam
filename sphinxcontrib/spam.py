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


class spam(nodes.Admonition, nodes.Element):
    pass


def visit_spam_node(self, node):
    self.visit_admonition(node)


def depart_spam_node(self, node):
    self.depart_admonition(node)


class SpamDirective(Directive):
    # この変数をセットすると、ディレクティブの中に
    # コンテンツを書けるようになります。
    has_content = True

    def run(self):
        env = self.state.document.settings.env

        ad = make_admonition(spam, self.name, ['Spam'], self.options,
                             self.content, self.lineno, self.content_offset,
                             self.block_text, self.state, self.state_machine)

        if not hasattr(env, 'spam_all_spams'):
            env.spam_all_spams = []
        env.spam_all_spams.append({
            'docname': env.docname,
            'lineno': self.lineno,
            'todo': ad[0].deepcopy(),
        })

        return ad


def write_spam(app, doctree, fromdocname):
    env = app.builder.env
    for spam_info in env.spam_all_spams:
        para = nodes.paragraph()
        filename = env.doc2path(spam_info['docname'], base=None)
        description = \
                '(The original entry is located in %s, line %d and can be found ' \
                % (filename, spam_info['lineno'])
        para += nodes.Text(description, description)
        para += 'spam! spam! spam!'
        para += nodes.Text('.)', '.)')


def setup(app):
    u'''setup

    see http://sphinx.shibu.jp/ext/tutorial.html
    '''
    app.add_node(spam,
            html=(visit_spam_node, depart_spam_node),
            latex=(visit_spam_node, depart_spam_node),
            text=(visit_spam_node, depart_spam_node))
    app.add_directive('spam', SpamDirective)
    app.connect("doctree-resolved", write_spam)
