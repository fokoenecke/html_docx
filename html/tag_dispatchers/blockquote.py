# encoding: utf-8
from mindboard.helpers.docx.html.tag_dispatchers import TagDispatcher


class BlockquoteDispatcher(TagDispatcher):
    def __init__(self):
        super(BlockquoteDispatcher, self).__init__()

    @classmethod
    def append_head(cls, element, container):
        return cls._append_blockquote(container)

    @classmethod
    def append_tail(cls, element, container):
        return cls._append_blockquote(container)

    @classmethod
    def _append_blockquote(cls, container):
        """
        <blockquote> creates a quote styled paragraph inside a docx container element.
        """
        return container
