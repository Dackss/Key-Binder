from pynput import keyboard, mouse

from src.files.key_mapping import key_mapping


class InputListener:
    def __init__(self, app):
        self.app = app
        self.keyboard_listener = None
        self.mouse_listener = None
        self.is_listening = False
        self.key_mapping = key_mapping

    def on_press(self, key):
        try:
            text = f'Touche {key.char} pressée\n'
            self.app.chat_box.append(text)
        except AttributeError:
            text = f'Touche {key} pressée\n'
            self.app.chat_box.append(text)

    def on_release(self, key):
        text = f'Touche relâchée : {key}\n'
        self.app.chat_box.append(text)

    def on_click(self, x, y, button, pressed):
        action = "Pressed" if pressed else "Released"
        self.app.chat_box.append(f'Mouse {button.name} {action}\n')

        key_base = self.app.key_base
        key_value = self.app.key_value

        if button == mouse.Button.right:
            if pressed:
                # Shift est pressé lors du clic droit
                keyboard.Controller().press(keyboard.Key.shift)
            else:
                # Shift est relâché lors du relâchement du clic droit
                keyboard.Controller().release(keyboard.Key.shift)

        """else key_base and key_value:
            if key_base in self.key_mapping:
                mapped_key = self.key_mapping[key_base]
                if button == mouse.Button.right and pressed:
                    keyboard.Controller().press(mapped_key)
                elif button == mouse.Button.right and not pressed:
                    keyboard.Controller().release(mapped_key)"""

    def toggle_listening(self):
        if self.is_listening:
            self.stop_listening()
        else:
            self.start_listening()

    def start_listening(self):
        self.keyboard_listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        self.mouse_listener = mouse.Listener(
            on_click=self.on_click
        )

        self.keyboard_listener.start()
        self.mouse_listener.start()
        self.is_listening = True

    def stop_listening(self):
        if self.keyboard_listener:
            self.keyboard_listener.stop()
            self.keyboard_listener = None
        if self.mouse_listener:
            self.mouse_listener.stop()
            self.mouse_listener = None
        self.is_listening = False
