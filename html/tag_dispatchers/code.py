# encoding: utf-8
from docx.text import Paragraph
from mindboard.helpers.docx.html.tag_dispatchers import TagDispatcher


class CodeDispatcher(TagDispatcher):
    def __init__(self):
        super(CodeDispatcher, self).__init__()

    @classmethod
    def append_head(cls, element, container):
        return cls._append_code(element.text, container)

    @classmethod
    def append_tail(cls, element, container):
        return cls._append_code(element.tail, container)

    @classmethod
    def _append_code(cls, text, container):
        """
        <code> Creates a specially styled run inside the given container.
        """
        #TODO find out how to monospace in oodocx
        monospace_style = 'NoSpacing'

        paragraph = cls.get_new_paragraph(container)
        paragraph.text = text
        paragraph.style = monospace_style

        return paragraph