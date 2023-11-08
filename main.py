from PyQt5 import QtWidgets
from src.files.app import App


def main():
    app = QtWidgets.QApplication([])
    window = App()
    app.exec_()


if __name__ == "__main__":
    main()
