# encoding: utf-8
from docx.enum.text import WD_BREAK
from mindboard.helpers.docx.html.tag_dispatchers import TagDispatcher, replace_whitespaces


class LineBreakDispatcher(TagDispatcher):
    def __init__(self):
        super(LineBreakDispatcher, self).__init__()

    @classmethod
    def append_head(cls, element, container):
        return cls._append_line_break(element, container)

    @classmethod
    def append_tail(cls, element, container):
        pass

    @classmethod
    def _append_line_break(cls, element, container):
        """
        <br> Creates a break item inside the given container.
        """
        element.tail = replace_whitespaces(element.tail)
        element.tail = element.tail.lstrip()

        run = container.add_run()
        run.add_break(break_type=WD_BREAK.LINE_CLEAR_RIGHT)
        return container
