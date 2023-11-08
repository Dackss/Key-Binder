from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox, QTextEdit, QInputDialog, QShortcut, QLabel, QVBoxLayout, QDialog

from src.files.input_listener import InputListener
from src.files.keybind_window import KeyBindWindow


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.key_label = None
        self.key_base = None
        self.on_release = None
        self.on_press = None
        self.listener = InputListener(self)
        self.key_value = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Key Binder")
        self.setWindowIcon(QtGui.QIcon("src/assets/logo.png"))
        self.setGeometry(100, 100, 575, 350)

        element_info = [
            {"type": QtWidgets.QLabel, "text": "Output", "font_size": 15, "geometry": (400, 8, 250, 20)},
            {"type": QTextEdit, "name": "chat_box", "font_size": 9, "geometry": (300, 30, 250, 300), "read_only": True},
            {"type": QtWidgets.QLabel, "name": "key_label", "text": "No key bound", "font_size": 9,
             "geometry": (150, 200, 250, 20)},
            {"type": QtWidgets.QDialogButtonBox, "name": "button_box", "font_size": 9,
             "geometry": (300, 330, 250, 50)},
            {"type": QtWidgets.QLabel, "name": "base_key", "text": "Base Key: None", "font_size": 10,
             "geometry": (150, 50, 250, 20)},
        ]

        for info in element_info:
            element = info["type"](self)
            if "text" in info:
                element.setText(info["text"])
            if "name" in info:
                setattr(self, info["name"], element)
            if "font_size" in info:
                element.setFont(QtGui.QFont("Arial", info["font_size"]))
            if "geometry" in info:
                element.setGeometry(*info["geometry"])
            if "read_only" in info:
                element.setReadOnly(info["read_only"])

        button_info = [
            ["Start (F11)", self.listener.start_listening, 110, 35, 20, 150],
            ["Stop (F11)", self.listener.stop_listening, 110, 35, 150, 150],
            ["Key to Bind", self.bind_key_pressed, 110, 35, 20, 200],
            ["Bind Base Key", self.bind_base_key_pressed, 110, 35, 20, 50]
        ]

        for label, callback, width, height, x, y in button_info:
            button = QtWidgets.QPushButton(label, self)
            button.clicked.connect(callback)
            button.setFixedSize(width, height)
            button.move(x, y)

        self.update_button_style()

        self.show()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def update_button_style(self):
        active_color = QtGui.QColor(200, 200, 200)
        inactive_color = QtGui.QColor(255, 255, 255)

        for button in self.findChildren(QtWidgets.QPushButton):
            if button.isChecked():
                if button.text() == "Stop (F11)":
                    button.setStyleSheet(f"background-color: {inactive_color.name()};")
                else:
                    button.setStyleSheet(f"background-color: {active_color.name()};")
            else:
                button.setStyleSheet(f"background-color: {inactive_color.name()};")

    def bind_key(self, callback):
        key_bind_window = KeyBindWindow(self)
        key_bind_window.keyPressed.connect(callback)
        key_bind_window.exec_()

    def handle_key_pressed(self, key_name):
        if key_name and key_name != "Waiting...":
            self.key_value = key_name
            self.key_label.setText(f"Key to Bind: {key_name}")
            print(f"Key to bind set to {key_name}")

    def bind_key_pressed(self):
        self.bind_key(self.handle_key_pressed)

    def handle_base_key_pressed(self, key_name):
        if key_name and key_name != "Waiting...":
            self.key_base = key_name
            self.base_key.setText(f"Base Key: {key_name}")
            print(f"Base key set to {key_name}")

    def bind_base_key_pressed(self):
        self.bind_key(self.handle_base_key_pressed)

    def bind_actions(self):
        if self.key_value is not None and self.key_base is not None:
            # Perform actions associated with the bound key and base key
            print(f"Key {self.key_value} pressed")
            print(f"Base key: {self.key_base}")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F11:
            self.listener.toggle_listening()
            self.update_button_style()

    def closeEvent(self, event):
        self.listener.stop_listening()
        super().closeEvent(event)
