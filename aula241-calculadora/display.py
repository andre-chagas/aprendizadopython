from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from utils import isEmpty, isNumOrDot
from variables import BIG_FONT_SIZE, MINIMUM_WIDHT, TEXT_MARGIN


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

        self.setReadOnly(True)

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDHT)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [Qt.Key.Key_Enter, Qt.Key.Key_Return, Qt.Key.Key_Equal]
        isDelete = key in [Qt.Key.Key_Backspace, Qt.Key.Key_Delete, Qt.Key.Key_D]
        isEsc = key in [Qt.Key.Key_Escape, Qt.Key.Key_C]
        isOperator = key in [
            Qt.Key.Key_Plus, Qt.Key.Key_Minus, Qt.Key.Key_Slash, Qt.Key.Key_Asterisk,
            Qt.Key.Key_Percent
        ]

        if isEnter:
            self.eqPressed.emit()
            return event.ignore()

        if isDelete:
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            self.clearPressed.emit()
            return event.ignore()

        if isOperator:
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()

        # Não passar daqui senão tiver texto
        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()