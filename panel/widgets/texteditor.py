"""
Defines a TextEditor widget based on quill.js.
"""
import param

from pyviz_comms import JupyterComm

from ..util import lazy_load
from .base import Widget


class TextEditor(Widget):
    """
    TextEditor widget allow editing text using the quill.js library.
    """

    disabled = param.Boolean(default=False, doc="""
        Whether the editor is disabled.""")

    mode = param.Selector(default='toolbar', objects=['bubble', 'toolbar'], doc="""
        Whether to display a toolbar or a bubble menu on highlight.""")

    toolbar = param.ClassSelector(default=True, class_=(list, bool), doc="""
        Toolbar configuration either as a boolean toggle or a configuration
        specified as a list.""")

    placeholder = param.String(doc="Placeholder output when the editor is empty.")

    value = param.String(doc="State of the current text in the editor")

    _rename = {"value": "text"}

    def _get_model(self, doc, root=None, parent=None, comm=None):
        if self._widget_type is None:
            self._widget_type = lazy_load(
                'panel.models.quill', 'QuillInput', isinstance(comm, JupyterComm), root
            )
        return super()._get_model(doc, root, parent, comm)
