from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from src.files.CustomButton import CustomButton
from PyQt5.QtCore import QPropertyAnimation
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
        self.setWindowTitle("Key Binder")
        self.setWindowIcon(QtGui.QIcon("src/assets/logo.png"))
        self.setGeometry(100, 100, 575, 350)

        self.setStyleSheet("""
            background-color: #D1D2D4;
            font-family: Lucida;
        """)

        element_info = [
            {"type": QtWidgets.QLabel, "text": "Output", "font_size": 15, "geometry": (400, 8, 250, 20)},
            {"type": QtWidgets.QTextEdit, "name": "chat_box", "font_size": 12, "geometry": (300, 30, 250, 230),
             "read_only": True, "border_radius": 10},
            {"type": QtWidgets.QLabel, "name": "key_label", "text": "No key bound", "font_size": 12,
             "geometry": (150, 200, 250, 20)},
            {"type": QtWidgets.QDialogButtonBox, "name": "button_box", "font_size": 12,
             "geometry": (300, 310, 250, 50)},
            {"type": QtWidgets.QLabel, "name": "base_key", "text": "Base Key: None", "font_size": 12,
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

        # Animation d'opacité pour la text box
        self.chat_box_opacity_animation = QPropertyAnimation(self.chat_box.document(), b"opacity")
        self.chat_box_opacity_animation.setDuration(500)
        self.chat_box_opacity_animation.setStartValue(0.0)
        self.chat_box_opacity_animation.setEndValue(1.0)

        # Ajout de l'effet d'opacité à la text box
        opacity_effect = QGraphicsOpacityEffect(self.chat_box)
        self.chat_box.setGraphicsEffect(opacity_effect)

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
        key_bind_window = KeyBindWindow(self)
        key_bind_window.keyPressed.connect(callback)
        key_bind_window.exec_()

    def handle_key_pressed(self, key_name):
        if key_name and key_name != "Waiting...":
            self.key_value = key_name
            self.key_label.setText(f"Key to Bind: {key_name}")
            print(f"Key to bind set to {key_name}")
            self.chat_box_opacity_animation.start()

    def bind_key_pressed(self):
        self.bind_key(self.handle_key_pressed)

    def handle_base_key_pressed(self, key_name):
        if key_name and key_name != "Waiting...":
            self.key_base = key_name
            self.base_key.setText(f"Base Key: {key_name}")
            print(f"Base key set to {key_name}")
            self.chat_box_opacity_animation.start()

    def bind_base_key_pressed(self):
        self.bind_key(self.handle_base_key_pressed)

    def bind_actions(self):
        if self.key_value is not None and self.key_base is not None:
            print(f"Key {self.key_value} pressed")
            print(f"Base key: {self.key_base}")
