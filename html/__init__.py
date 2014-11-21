# encoding: utf-8

"""
Wrapper methods used for mapping HTML to docx objects
"""

from lxml.html import fromstring
from mindboard.helpers.docx.html.converter import DocxBuilder


def add_html(container, html_string):
    root = fromstring(html_string)
    builder = DocxBuilder(container=container)
    builder.from_html_tree(root=root)