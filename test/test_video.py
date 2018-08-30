# -*- coding: utf-8 -*-

import unittest
from kamchatka.peripheral.video import VideoAdapter


class VideoTestCase(unittest.TestCase):

    def setUp(self):
        self.video_adapter = VideoAdapter()

    def test_brightness_down(self):
        self.video_adapter.process('bd')

    # def brightness_up(self):
    #     self.video_adapter.process('bu')
