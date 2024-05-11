import os.path

from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import Qt, QSize

from qtharmony.src.core import StyleSheetLoader
from qtharmony.src.config import UI_RESOURCES

from qtharmony.src.core.theme import ThemeManager

from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from PySide6.QtGui import QFont
    from PySide6.QtWidgets import QWidget


class DropDownMenu(QComboBox):
    """
    Custom QComboBox widget for a drop-down menu.

    Methods:
    - __init__(values: Optional[list[str]] = None, size: tuple[int, int] = (200, 30),
              font: Optional["QFont"] = None, *, stylesheet: Optional[str] = None,
              parent: Optional["QWidget"] = None): None
              - Initializes the DropDownMenu widget with optional values, size, font, and stylesheet.
    - set_items(*__values: str) -> None
              - Sets the items in the drop-down menu with the provided values.
    """

    def __init__(
            self, 
            values: Optional[list[str]] = None, 
            size: tuple[int, int] = (200, 30),
            font: Optional["QFont"] = None, 
            *,
            stylesheet: Optional[str] = None,
            parent: Optional["QWidget"] = None
    ) -> None:
        """
        Initializes the DropDownMenu widget with optional values, size, font, and stylesheet.

        Args:
            values (Optional[list[str]], optional): List of values to populate the drop-down menu. Defaults to None.
            size (tuple[int, int], optional): The size of the drop-down menu widget (width, height). Defaults to (200, 30).
            font (Optional["QFont"], optional): The font to be used for the drop-down menu. Defaults to None.
            stylesheet (Optional[str], optional): Custom stylesheet for the drop-down menu widget. Defaults to None.
            parent (Optional["QWidget"], optional): Parent widget of the drop-down menu. Defaults to None.
        """

        super().__init__(parent)
        ThemeManager.add_widgets(self)

        self.setFixedSize(QSize(*size))
        self.view().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.__values = []

        if values is not None: self.__values = [*values]
        self.addItems(self.__values)
        self.setObjectName("drop-down-menu")
        if font is not None: self.setFont(font)

        self.setStyleSheet(StyleSheetLoader.load_stylesheet(
            __file__, "styles/drop_down_menu.css", 
            name="DropDownMenu", obj_name="QComboBox#drop-down-menu",
            stylesheet=stylesheet
        ))

        self.__load_down_arrow_style()
    
    def __load_down_arrow_style(self) -> None:
        """
        Loads the custom style for the drop-down arrow in the DropDownMenu widget.
        """

        down_arrow = (
            "\nDropDownMenu::down-arrow {" 
            + f"image: url({os.path.join(UI_RESOURCES, 'angle-down.png')})" 
            + "}"
        )

        self.setStyleSheet(StyleSheetLoader.append_stylesheet(
            self.styleSheet(), down_arrow, 
            name="DropDownMenu", obj_name="QComboBox#drop-down-menu"
        ))

    def set_items(self, *__values: str) -> None:
        """
        Sets the items in the drop-down menu with the provided values.

        Args:
            *__values (str): Variable number of values to populate the drop-down menu.
        """
    
        self.__values = [*__values]
        self.addItems(self.__values)

