from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, QSize

from qtharmony.src.core import StyleSheetLoader
from qtharmony.src.core.theme import ThemeManager

from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from PySide6.QtGui import QFont
    from PySide6.QtWidgets import QWidget


class Entry(QLineEdit):
    """
    Custom QLineEdit widget for text input.

    Methods:
    - __init__(placed: Optional[str] = None, placeholder: Optional[str] = None, size: tuple[int, int] = (200, 30),
              font: Optional["QFont"] = None, *, stylesheet: Optional[str] = None, parent: Optional["QWidget"] = None): None
              - Initializes the Entry widget with optional text, placeholder, size, font, and stylesheet.
    """

    def __init__(
            self, 
            placed: Optional[str] = None, 
            placeholder: Optional[str] = None,
            size: Optional[tuple[int, int]] = None, 
            font: Optional["QFont"] = None, 
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        """
        Initializes the Entry widget with optional text, placeholder, size, font, and stylesheet.

        Args:
            placed (Optional[str], optional): The initial text to be displayed in the entry. Defaults to None.
            placeholder (Optional[str], optional): The placeholder text to be displayed when the entry is empty. Defaults to None.
            size (tuple[int, int], optional): The size of the entry widget (width, height). Defaults to (200, 30).
            font (Optional["QFont"], optional): The font to be used for text input. Defaults to None.
            stylesheet (Optional[str], optional): Custom stylesheet for the entry widget. Defaults to None.
            parent (Optional["QWidget"], optional): Parent widget of the entry. Defaults to None.
        """

        super().__init__(parent)
        ThemeManager.add_widgets(self)

        if placed is not None: self.setText(placed)
        if placeholder is not None: self.setPlaceholderText(placeholder)
        if font is not None: self.setFont(font)
        if size is not None: self.setFixedSize(*size)

        self.setObjectName("entry")
        self.setFocusPolicy(Qt.FocusPolicy.WheelFocus)

        self.stylesheet = StyleSheetLoader.load_stylesheet(
            __file__, "styles/entry.css", 
            name="Entry", obj_name="QLineEdit#entry",
            stylesheet=stylesheet
        )
