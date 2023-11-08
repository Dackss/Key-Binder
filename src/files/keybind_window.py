from PyQt5 import QtWidgets, QtGui, QtCore


class KeyBindWindow(QtWidgets.QDialog):
    keyPressed = QtCore.pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Select a Key")
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.setFixedSize(300, 100)
        self.label = QtWidgets.QLabel("Waiting...", self)
        self.label.setGeometry(QtCore.QRect(80, 30, 150, 30))
        self.label.setFont(QtGui.QFont("Arial", 12))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowIcon(QtGui.QIcon("src/assets/logo.png"))

    def keyPressEvent(self, event):
        if event.type() == QtCore.QEvent.KeyPress:
            modifiers = event.modifiers()
            key_name = self.get_key_name(event.key(), modifiers)
            self.keyPressed.emit(key_name)
            self.close()

    def mousePressEvent(self, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            button_name = self.get_mouse_button_name(event.button())
            self.keyPressed.emit(button_name)
            self.close()

    def get_key_name(self, key, modifiers):
        if key == QtCore.Qt.Key_Shift:
            return "Shift"
        elif key == QtCore.Qt.Key_Control:
            return "Ctrl"
        elif key == QtCore.Qt.Key_Alt:
            return "Alt"
        elif key == QtCore.Qt.Key_Meta:
            return "Meta"
        key_sequence = QtGui.QKeySequence(key)
        key_name = key_sequence.toString(QtGui.QKeySequence.NativeText)
        if modifiers & QtCore.Qt.ShiftModifier:
            key_name = "Shift+" + key_name
        if modifiers & QtCore.Qt.ControlModifier:
            key_name = "Ctrl+" + key_name
        if modifiers & QtCore.Qt.AltModifier:
            key_name = "Alt+" + key_name
        if modifiers & QtCore.Qt.MetaModifier:
            key_name = "Meta+" + key_name
        return key_name

    def get_mouse_button_name(self, button):
        if button == QtCore.Qt.LeftButton:
            return "Left Button"
        elif button == QtCore.Qt.RightButton:
            return "Right Button"
        elif button == QtCore.Qt.MiddleButton:
            return "Middle Button"
        elif button == QtCore.Qt.BackButton:
            return "Back Button"
        elif button == QtCore.Qt.ForwardButton:
            return "Forward Button"
        elif button == QtCore.Qt.WheelButton:
            return "Wheel Button"
        else:
            return "Unknown Button"

    def get_selected_key(self):
        return self.label.text()
