# encoding: utf-8

# map of HTML list tags and their docx styles
from mindboard.helpers.docx.html.tag_dispatchers import TagDispatcher, replace_whitespaces

_list_style = dict(
    ol='ListNumber',
    ul='ListBullet',
)


class ListItemDispatcher(TagDispatcher):
    def __init__(self):
        super(ListItemDispatcher, self).__init__()

    @classmethod
    def append_head(cls, element, container):
        paragraph = cls.get_new_paragraph(container)
        return cls._append_list_item(element, element.text, paragraph)

    @classmethod
    def append_tail(cls, element, container):
        paragraph = cls.get_current_paragraph(container)
        return cls._append_list_item(element, element.tail, paragraph)

    @classmethod
    def _append_list_item(cls, element, text, container):
        """
        <li> Create a list item element inside a docx container.
        Style it according to its parents list type.
        """
        text = replace_whitespaces(text)
        text = '' if text == ' ' else text

        style = _list_style.get(element.getparent().tag, 'ListBullet')
        container.style = style
        container.add_run(text)

        return container