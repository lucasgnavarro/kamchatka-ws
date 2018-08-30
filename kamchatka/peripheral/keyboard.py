# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from pykeyboard import PyKeyboard
import platform


class GenericKeyboard(ABC):

    def __init__(self, ):
        self.mapped_actions = {
            'wfs': self.window_focus_start,
            'wff': self.window_focus_finish,
            'bnt': self.browser_next_tab,
            'bpt': self.browser_previous_tab,
            'bot': self.browser_open_tab,
            'bct': self.browser_close_tab,
            'fn': self.focus_next,
            'fp': self.focus_previous,
            'ua': self.up_arrow,
            'da': self.down_arrow,
            'la': self.left_arrow,
            'ra': self.right_arrow,
            'kp': self.key_press
        }

        self.keyboard = self.get_keyboard()
        super().__init__()

    def get_keyboard(self):
        return PyKeyboard()

    def combinate_keys(self, pressed_keys=None, tap_key=None, to_release_key=None):
        """
        Allows the combination of keys, like ctrl+alt+supr
        :param pressed_keys: Array of keys to hold down
        :param tap_key: Key to tap in the combination
        :return:
        """
        _pressed_keys = [] if pressed_keys is None else pressed_keys
        for key in _pressed_keys:    # Loop through to_press array and press keys
            self.keyboard.press_key(key)

        if tap_key is not None:  # If to_tap key is defined
            self.keyboard.tap_key(tap_key)

    def release_keys(self, keys=None):
        """
        Release keys function
        :param keys: Array of keys to release
        :return:
        """
        _keys = [] if keys is None else keys
        if type([]) != type(_keys):
            _keys = [_keys]

        for key in _keys:
            self.keyboard.release_key(key)

    def tap_key(self, key=None):
        """
        Press and release char
        :param key: key to press and release
        :return:
        """
        if key is not None:
            self.keyboard.tap_key(key)

    def window_focus_start(self):
        """
        Simulate Alt + Tab for change window focus
        :return:
        """
        self.release_keys([self.keyboard.alt_key])
        self.combinate_keys([self.keyboard.alt_key], self.keyboard.tab_key)

    def window_focus_finish(self):
        """
        Finish the Alt + Tab simulation
        :return:
        """
        self.release_keys([self.keyboard.tab_key, self.keyboard.alt_key])

    def browser_next_tab(self):
        """
        Change to next tab in open browser
        :return:
        """
        self.combinate_keys([self.keyboard.control_l_key],self.keyboard.tab_key)
        self.release_keys([self.keyboard.control_l_key])

    def browser_previous_tab(self):
        """
        Change to previous tab in open browser
        :return:
        """
        self.combinate_keys([self.keyboard.control_l_key, self.keyboard.shift_key], self.keyboard.tab_key)
        self.release_keys([self.keyboard.control_l_key, self.keyboard.shift_key])

    def browser_open_tab(self):
        """
        Open new tab in open browser
        :return:
        """
        self.release_keys([self.keyboard.control_l_key])
        self.combinate_keys([self.keyboard.control_l_key], 't')
        self.release_keys([self.keyboard.control_l_key])

    def browser_close_tab(self):
        """
        Close current tab in open browser
        :return:
        """
        self.release_keys([self.keyboard.control_l_key])
        self.combinate_keys([self.keyboard.control_l_key], self.keyboard.function_keys[4])
        self.release_keys([self.keyboard.control_l_key])

    def focus_next(self):
        """
        Simulate focus change, with TAB key
        :return:
        """
        self.tap_key(self.keyboard.tab_key)

    def focus_previous(self):
        """
        Simulate focus prev change, with SHIFT + TAB key
        :return:
        """
        self.combinate_keys([self.keyboard.shift_key], self.keyboard.tab_key)
        self.release_keys([self.keyboard.shift_key])

    def up_arrow(self):
        """
        Tap UP ARROW
        :return:
        """
        self.tap_key(self.keyboard.up_key)

    def down_arrow(self):
        """
        Tap DOWN ARROW
        :return:
        """
        self.tap_key(self.keyboard.down_key)

    def left_arrow(self):
        """
        Tap LEFT ARROW
        :return:
        """
        self.tap_key(self.keyboard.left_key)

    def right_arrow(self):
        """
        Tap RIGHT ARROW
        :return:
        """
        self.tap_key(self.keyboard.right_key)

    def key_press(self, value=''):
        special_keys = {
            'enterKey': self.keyboard.enter_key,
            'backSpace': self.keyboard.backspace_key,
            'spaceKey': ' '
        }
        if value in special_keys:
            self.keyboard.tap_key(special_keys[value])
        else:
            self.keyboard.tap_key(value)

    def process(self, action=None, value=None):
        _action = self.mapped_actions.get(action)

        if _action is not None:
            if value is None:
                return _action()
            else:
                return _action(value)
        else:
            raise Exception('Action {} is not defined in Generic Keyboard'.format(action))


class LinuxKeyboard(GenericKeyboard):
    pass


class WindowKeyboard(GenericKeyboard):
    pass


class MacKeyboard(GenericKeyboard):
    pass


class Keyboard:
    _keyboards = {
        'Linux': LinuxKeyboard,
        'Windows': WindowKeyboard,
        'Darwin': MacKeyboard
    }

    def __init__(self):
        self.current_keyboard = self.get_keyboard()

    def get_keyboard(self):
        _keyboard = self._keyboards.get(platform.system())

        if _keyboard is not None:
            return _keyboard()
        else:
            raise Exception('Keyboard is Invalid, system {}'.format(platform.system()))

    def process(self, action='', value=None):
        return self.current_keyboard.process(action, value)

