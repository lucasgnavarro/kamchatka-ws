# -*- coding: utf-8 -*-
import unittest
from kamchatka.peripheral.audio import SoundMixer


class AudioTestCase(unittest.TestCase):

    def setUp(self):
        self.mixer = SoundMixer()

    def test_volume_down(self):
        print('Test Volume Down')
        self.mixer.process('vd')

    def test_volume_up(self):
        print('Test Volume Up')
        self.mixer.process('vu')

    def test_volume_mute(self):
        print('Test Volume Mute')
        self.mixer.process('vm')

    def test_volume_unmute(self):
        print('Test Volume Unmute')
        self.mixer.process('vt')

