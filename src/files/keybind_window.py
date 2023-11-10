from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QEvent


class KeyBindWindow(QtWidgets.QDialog):
    keyPressed = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Select a Key")
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.setFixedSize(300, 100)
        self.label = QtWidgets.QLabel("Waiting...", self)
        self.label.setGeometry(QtCore.QRect(80, 30, 150, 30))
        self.label.setFont(QtGui.QFont("Arial", 12))
        self.label.setAlignment(Qt.AlignCenter)
        self.setWindowIcon(QtGui.QIcon("src/assets/logo.png"))

    def keyPressEvent(self, event):
        try:
            if event.type() == QEvent.KeyPress:
                modifiers = event.modifiers()
                key_name = self.get_key_name(event.key(), modifiers)
                self.keyPressed.emit(key_name if key_name else "No key pressed")
                self.close()
        except Exception as e:
            print(f"Error in keyPressEvent: {e}")

    def mousePressEvent(self, event):
        try:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                button_name = self.get_mouse_button_name(event.button())
                if button_name:
                    self.keyPressed.emit(button_name)
                else:
                    self.keyPressed.emit("No key pressed")
                self.close()
        except Exception as e:
            print(f"Error in mousePressEvent: {e}")

    @staticmethod
    def get_key_name(key, modifiers):
        if key == Qt.Key_Shift:
            return "Shift"
        elif key == Qt.Key_Control:
            return "Ctrl"
        elif key == Qt.Key_Alt:
            return "Alt"
        elif key == Qt.Key_Meta:
            return "Meta"
        key_sequence = QtGui.QKeySequence(key)
        key_name = key_sequence.toString(QtGui.QKeySequence.NativeText)
        if modifiers & Qt.ShiftModifier:
            key_name = "Shift+" + key_name
        if modifiers & Qt.ControlModifier:
            key_name = "Ctrl+" + key_name
        if modifiers & Qt.AltModifier:
            key_name = "Alt+" + key_name
        if modifiers & Qt.MetaModifier:
            key_name = "Meta+" + key_name
        return key_name

    @staticmethod
    def get_mouse_button_name(button):
        if button == Qt.LeftButton:
            return "Left Button"
        elif button == Qt.RightButton:
            return "Right Button"
        elif button == Qt.MiddleButton:
            return "Middle Button"
        elif button == Qt.BackButton:
            return "Back Button"
        elif button == Qt.ForwardButton:
            return "Forward Button"
        elif button == Qt.WheelButton:
            return "Wheel Button"
        else:
            return "Unknown Button"

    def get_selected_key(self):
        return self.label.text()
