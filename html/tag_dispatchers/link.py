# encoding: utf-8
from mindboard.helpers.docx.html.tag_dispatchers import TagDispatcher


class LinkDispatcher(TagDispatcher):
    def __init__(self):
        super(LinkDispatcher, self).__init__()

    @classmethod
    def append_head(cls, element, container):
        return cls._append_link(element.text, container)

    @classmethod
    def append_tail(cls, element, container):
        return cls._append_link(element.tail, container)

    @classmethod
    def _append_link(cls, text, container):
        """
        <a> creates a link element inside a docx container element.
        """
        container.add_run(text=text)
        return container
