from PyQt5 import QtWidgets, QtGui, QtCore
from src.files.CustomButton import CustomButton

from src.files.input_listener import InputListener
from src.files.keybind_window import KeyBindWindow


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.chat_box_opacity_animation = None
        self.key_label = None
        self.key_base = None
        self.listener = InputListener(self)
        self.key_value = None
        self.init_ui()

    def init_ui(self):
        """import sys
        sys.excepthook = sys.__excepthook__

        def exception_hook(exctype, value, traceback):
            print(exctype, value, traceback)
            sys.__excepthook__(exctype, value, traceback)

        sys.excepthook = exception_hook"""

        self.setWindowTitle("Key Binder")
        self.setWindowIcon(QtGui.QIcon("src/assets/logo.png"))
        self.setGeometry(900, 500, 600, 275)

        self.setStyleSheet("""
            background-color: #D1D2D4;
            font-family: Lucida;
        """)

        element_info = [
            {"type": QtWidgets.QLabel, "text": "Output", "font_size": 15, "geometry": (400, 5, 250, 30)},
            {"type": QtWidgets.QTextEdit, "name": "chat_box", "font_size": 8, "geometry": (335, 40, 250, 230),
             "read_only": True, "border_radius": 10, "background_color": "#EAEAEA"},
            {"type": QtWidgets.QLabel, "name": "key_label", "text": "No key bound", "font_size": 8,
             "geometry": (150, 200, 180, 30)},
            {"type": QtWidgets.QDialogButtonBox, "name": "button_box", "font_size": 12,
             "geometry": (300, 310, 250, 50)},
            {"type": QtWidgets.QLabel, "name": "base_key", "text": "Base Key: None", "font_size": 8,
             "geometry": (150, 50, 180, 30)},
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
            if "background_color" in info:
                element.setStyleSheet(f"background-color: {info['background_color']};")

        button_info = [
            ["Start (F11)", self.listener.start_listening, 110, 35, 20, 150],
            ["Stop (F11)", self.listener.stop_listening, 110, 35, 150, 150],
            ["Key to Bind", self.bind_key_pressed, 110, 35, 20, 200],
            ["Bind Base Key", self.bind_base_key_pressed, 110, 35, 20, 50]
        ]

        for label, callback, width, height, x, y in button_info:
            button = CustomButton(label, self)
            button.clicked.connect(callback)
            button.setFixedSize(width, height)
            button.move(x, y)

        self.show()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def bind_key(self, callback):
        try:
            key_bind_window = KeyBindWindow(self)
            key_bind_window.keyPressed.connect(callback)
            key_bind_window.exec_()
        except Exception as e:
            print(f"Erreur dans bind_key : {e}")

    def handle_key_pressed(self, key_name):
        try:
            if key_name and key_name != "Waiting...":
                self.key_value = key_name
                self.key_label.setText(f"Key to Bind: {key_name}")
                print(f"Key to bind set to {key_name}")
                self.chat_box_opacity_animation.start()
        except Exception as e:
            print(f"Erreur dans handle_key_pressed : {e}")

    def bind_key_pressed(self):
        try:
            self.bind_key(self.handle_key_pressed)
        except Exception as e:
            print(f"Erreur dans bind_key_pressed : {e}")

    def handle_base_key_pressed(self, key_name):
        try:
            if key_name and key_name != "Waiting...":
                self.key_base = key_name
                self.base_key.setText(f"Base Key: {key_name}")
                print(f"Base key set to {key_name}")
                self.chat_box_opacity_animation.start()
        except Exception as e:
            print(f"Erreur dans handle_base_key_pressed : {e}")

    def bind_base_key_pressed(self):
        try:
            self.bind_key(self.handle_base_key_pressed)
        except Exception as e:
            print(f"Erreur dans bind_base_key_pressed : {e}")

    def bind_actions(self):
        try:
            if self.key_value is not None and self.key_base is not None:
                print(f"Key {self.key_value} pressed")
                print(f"Base key: {self.key_base}")
        except Exception as e:
            print(f"Erreur dans bind_actions : {e}")
