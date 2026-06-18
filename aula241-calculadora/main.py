import sys

from buttons import ButtonsGrid
from display import Display
from files.styles import setupTheme
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH

print("Iniciando...")

if __name__ == '__main__':
    # Cria a aplicação
    
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()
    
    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    # info = Info('Sua conta')
    # window.vLayout.addWidget(info)

    # Display
    # display = Display()
    # window.vLayout.addWidget(display)

    # Grid
    # buttonsGrid = ButtonsGrid(display, info, window)
    # window.vLayout.addLayout(buttonsGrid)
    
    # Executa tudo
    window.adjustSize()
    window.show()
    print("Janela aberta!")
    app.exec()

   