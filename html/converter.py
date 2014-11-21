# encoding: utf-8

"""
Converter recursively iterating over HTML ElementTree(etree)
mapping HTML tags to their corresponding python-docx functions.
Appending full HTML structure to the given document.
"""
from mindboard.helpers.docx.html.dispatcher import get_tag_dispatcher


class DocxBuilder(object):
    """
    Taking the root container our html should be appended to
    """
    def __init__(self, container):
        super(DocxBuilder, self).__init__()
        self._root_container = container

    def from_html_tree(self, root):
        """
        Appending all the HTML elements, beginning at root object
        """
        self._append_docx_elements(root, self._root_container)

    def _append_docx_elements(self, html_element, container):
        """
        Retrieving and calling a creating object for
        the given HTML tag. Recursive call for all
        children of the element.
        """
        dispatcher = get_tag_dispatcher(html_element.tag)
        # only call when a function is attached to tag
        new_container = container
        if dispatcher:
            new_container = dispatcher.append_head(html_element, container)

        children = list(html_element)
        for child in children:
            self._append_docx_elements(child, new_container)

        dispatcher = get_tag_dispatcher(html_element.getparent().tag)
        if html_element.tail and dispatcher:
            dispatcher.append_tail(html_element, container)
