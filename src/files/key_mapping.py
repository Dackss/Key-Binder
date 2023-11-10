from pynput import keyboard

key_mapping = {
    "A": keyboard.KeyCode.from_char('a'), "B": keyboard.KeyCode.from_char('b'), "C": keyboard.KeyCode.from_char('c'),
    "D": keyboard.KeyCode.from_char('d'), "E": keyboard.KeyCode.from_char('e'), "F": keyboard.KeyCode.from_char('f'),
    "G": keyboard.KeyCode.from_char('g'), "H": keyboard.KeyCode.from_char('h'), "I": keyboard.KeyCode.from_char('i'),
    "J": keyboard.KeyCode.from_char('j'), "K": keyboard.KeyCode.from_char('k'), "L": keyboard.KeyCode.from_char('l'),
    "M": keyboard.KeyCode.from_char('m'), "N": keyboard.KeyCode.from_char('n'), "O": keyboard.KeyCode.from_char('o'),
    "P": keyboard.KeyCode.from_char('p'), "Q": keyboard.KeyCode.from_char('q'), "R": keyboard.KeyCode.from_char('r'),
    "S": keyboard.KeyCode.from_char('s'), "T": keyboard.KeyCode.from_char('t'), "U": keyboard.KeyCode.from_char('u'),
    "V": keyboard.KeyCode.from_char('v'), "W": keyboard.KeyCode.from_char('w'), "X": keyboard.KeyCode.from_char('x'),
    "Y": keyboard.KeyCode.from_char('y'), "Z": keyboard.KeyCode.from_char('z'),

    "F1": keyboard.Key.f1, "F2": keyboard.Key.f2, "F3": keyboard.Key.f3, "F4": keyboard.Key.f4,
    "F5": keyboard.Key.f5, "F6": keyboard.Key.f6, "F7": keyboard.Key.f7, "F8": keyboard.Key.f8,
    "F9": keyboard.Key.f9, "F10": keyboard.Key.f10, "F11": keyboard.Key.f11, "F12": keyboard.Key.f12,

    "ESC": keyboard.Key.esc, "TAB": keyboard.Key.tab, "CAPS": keyboard.Key.caps_lock,
    "SHIFT": keyboard.Key.shift, "CTRL": keyboard.Key.ctrl, "ALT": keyboard.Key.alt,
    "SPACE": keyboard.Key.space, "ENTER": keyboard.Key.enter, "BACKSPACE": keyboard.Key.backspace,
    "INSERT": keyboard.Key.insert, "DELETE": keyboard.Key.delete, "HOME": keyboard.Key.home,
    "END": keyboard.Key.end, "PAGEUP": keyboard.Key.page_up, "PAGEDOWN": keyboard.Key.page_down,
    "UP": keyboard.Key.up, "DOWN": keyboard.Key.down, "LEFT": keyboard.Key.left, "RIGHT": keyboard.Key.right,
    "NUMLOCK": keyboard.Key.num_lock, "SCROLLLOCK": keyboard.Key.scroll_lock, "PAUSE": keyboard.Key.pause,
    "PRINTSCREEN": keyboard.Key.print_screen, "WIN": keyboard.Key.cmd,
}
