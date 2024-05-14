from PySide6.QtWidgets import QSplitter
from PySide6.QtCore import Qt

from qtharmony.src.core import StyleSheetLoader
from qtharmony.src.core.theme import ThemeManager

from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from PySide6.QtWidgets import QWidget


class Splitter(QSplitter):
    """
    Custom QSplitter widget for managing layout splitting.

    Methods:
    - __init__(__orientation: str, *, parent=None): None - Initializes the splitter with a specified orientation.
    - addWidget(widget): None - Adds a widget to the splitter and sets it as non-collapsible.
    """

    def __init__(
            self, 
            __orientation: str,
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        """
        Initializes the Splitter instance with the specified orientation.

        Args:
            __orientation (str): The orientation of the splitter, either "horizontal" or "vertical".
            stylesheet (Optional[str], optional): Custom stylesheet for the splitter. Defaults to None.
            parent (Optional["QWidget"], optional): Parent widget of the splitter. Defaults to None.
        """

        if __orientation == "horizontal": super().__init__(Qt.Orientation.Horizontal, parent)
        elif __orientation == "vertical": super().__init__(Qt.Orientation.Vertical, parent)

        ThemeManager.add_widgets(self)

        self.setObjectName("splitter")
        self.stylesheet = StyleSheetLoader.load_stylesheet(
            __file__, "styles/splitter.css", 
            name=self.__class__.__name__, obj_name="QSplitter#splitter",
            stylesheet=stylesheet
        )

    def addWidget(self, widget):
        """
        Adds a widget to the splitter and sets it as non-collapsible.

        Args:
            widget (QWidget): The widget to be added to the splitter.
        """

        super().addWidget(widget)
        self.setCollapsible(self.indexOf(widget), False)

