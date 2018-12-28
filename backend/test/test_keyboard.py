import unittest
from kamchatka.peripheral.keyboard import Keyboard


class KeyboardTestCase(unittest.TestCase):

    def setUp(self):
        self.keyboard = Keyboard()

    def test_window_focus_start(self):
        self.keyboard.process('wfs')

    def test_window_focus_finish(self):
        self.keyboard.process('wff')

    def test_browser_next_tab(self):
        self.keyboard.process('bnt')

    def test_browser_previous_tab(self):
        self.keyboard.process('bpt')

    def test_browser_open_tab(self):
        self.keyboard.process('bot')

    def test_browser_close_tab(self):
        self.keyboard.process('bct')

    def test_focus_next(self):
        self.keyboard.process('fn')

    def test_focus_previous(self):
        self.keyboard.process('fp')

    def test_up_arrow(self):
        self.keyboard.process('ua')

    def test_down_arrow(self):
        self.keyboard.process('da')

    def test_left_arrow(self):
        self.keyboard.process('la')

    def test_right_arrow(self):
        self.keyboard.process('ra')

    def test_key_press(self):
        self.keyboard.process('kp', 'a')
        self.keyboard.process('kp', ' ')
        self.keyboard.process('kp', 'backSpace')
        self.keyboard.process('kp', 'backSpace')
        self.keyboard.process('kp', 'enterKey')

