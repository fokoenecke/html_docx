# encoding: utf-8
from mindboard.helpers.docx.html.tag_dispatchers import TagDispatcher, replace_whitespaces


class EmphasisDispatcher(TagDispatcher):
    def __init__(self):
        super(EmphasisDispatcher, self).__init__()

    @classmethod
    def append_head(cls, element, container):
        return cls._append_emphasis(element.text, element, container)

    @classmethod
    def append_tail(cls, element, container):
        return cls._append_emphasis(element.tail, element, container)

    @classmethod
    def _append_emphasis(cls, text, element, container):
        """
        <em> Creates an italic text run inside the paragraph container.
        Appends remainder of text as a additional run
        """
        text = replace_whitespaces(text)
        run = container.add_run(text=text)
        run.italic = True
        if element.getparent().tag == 'strong':
            run.bold = True
        return container