''' Arquivo principal para executar o programa'''
from PyQt5.QtWidgets import QApplication
from controller.TelaInicialController import LoginWindow
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    loginWindow = LoginWindow()
    loginWindow.show()
    app.exec_()