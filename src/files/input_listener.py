from pynput import keyboard, mouse
from pynput.keyboard import Key, Controller

from src.files.key_mapping import key_mapping


class InputListener:
    def __init__(self, app):
        self.app = app
        self.keyboard_listener = None
        self.mouse_listener = None
        self.is_listening = False
        self.key_mapping = key_mapping

    def on_press(self, key):
        key_name = self.get_key_name(key)
        self.app.chat_box.append(f"Touche {key_name} pressée\n")

        if self.app.key_base and key_name == self.app.key_base:
            with keyboard.Controller() as controller:
                mapped_key = self.get_mapped_key(self.app.key_value)
                controller.press(mapped_key)
                controller.release(mapped_key)

    def on_release(self, key):
        key_name = self.get_key_name(key)
        self.app.chat_box.append(f"Touche {key_name} relâchée\n")

    @staticmethod
    def get_key_name(key):
        try:
            return key.char  # Pour les touches standards
        except AttributeError:
            return key.name  # Pour les touches spéciales

    @staticmethod
    def get_mapped_key(key_value):
        special_keys = {
            'shift': keyboard.Key.shift,
            'ctrl': keyboard.Key.ctrl,
            'alt': keyboard.Key.alt,
            # Ajoutez d'autres touches spéciales si nécessaire
        }
        return special_keys.get(key_value.lower(), key_value)

    def on_click(self, x, y, button, pressed):
        action = "Pressed" if pressed else "Released"
        self.app.chat_box.append(f'Mouse {button.name} {action}\n')

        key_base = self.app.key_base
        key_value = self.app.key_value

        # Mapping des noms de boutons de souris aux objets pynput correspondants
        mouse_button_mapping = {
            "Left Button": mouse.Button.left,
            "Right Button": mouse.Button.right,
            "Middle Button": mouse.Button.middle
            # Ajoutez d'autres mappings si nécessaire
        }

        special_keys = {
            'shift': Key.shift,
            'ctrl': Key.ctrl,
            'alt': Key.alt,
            'esc': Key.esc,
            # Ajoutez d'autres touches spéciales si nécessaire
        }

        if key_base and key_value:
            if key_base in mouse_button_mapping and pressed:
                mapped_mouse_button = mouse_button_mapping[key_base]
                if button == mapped_mouse_button:
                    controller = keyboard.Controller()

                    # Convertir key_value en un objet de touche spécial si nécessaire
                    mapped_key = special_keys.get(key_value.lower(), key_value)

                    try:
                        controller.press(mapped_key)
                        controller.release(mapped_key)
                    except ValueError as e:
                        print(f"Erreur lors de la simulation de la touche : {e}")

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
