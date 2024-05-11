from PySide6.QtWidgets import (
    QWidget, QHBoxLayout
)

import sys

from qtharmony.widgets import *
from qtharmony.windows import MainWindow
from qtharmony.constructor import Initialization

from qtharmony.src.core.theme import ThemeBuilder

Initialization.init(sys.argv)


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.widgetsList = WidgetsList()

        ThemeBuilder("qtharmony/resources/themes/dark-default.json")

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(Label("Hello", "Noto Sans", 13))
        self.mainLayout.addWidget(PushButton("Button"))
        self.mainLayout.addWidget(DropDownMenu([str(i) for i in range(100)]))

        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    window = MainWindow(Window())
    window.show()

    Initialization.exec()
