# -*- coding : utf-8 -*-
import platform
from subprocess import call, check_call, check_output
from abc import ABC, abstractmethod


class GenericVideoAdapter(ABC):

    def __init__(self):
        self.mapped_actions = {
            'bd': self.brightness_down,
            'bu': self.brightness_up
        }
        self.brightness_scale = 10

    @abstractmethod
    def get_current_screen(self):
        pass

    @abstractmethod
    def get_current_brightness(self):
        pass

    @abstractmethod
    def brightness_up(self):
        pass

    @abstractmethod
    def brightness_down(self):
        pass

    def proccess(self, action):
        _action = self.mapped_actions.get(action)

        if _action is not None:
            return _action()
        else:
            raise Exception('Action {} is not defined in Generic Video Adapter'.format(action))


class LinuxVideoAdapter(GenericVideoAdapter):

    def get_current_screen(self):
        _screen = check_output("xrandr -q | grep ' connected' | cut -d ' ' -f1", shell=True).strip()

        try:
            _screen = _screen.decode('utf-8')
        except AttributeError:
            pass

        return _screen

    def get_current_brightness(self):
        return float(check_output("xrandr --verbose | grep -i brightness | cut -f2 -d ' '", shell=True).strip())

    def adjust_brightness(self, action=None):
        _factor = 1 if action == 'up' else -1   # if action is not 'up' then factor is negative
        new_brightness = self.get_current_brightness() + ((float(self.brightness_scale) / 100) * _factor)   # +(-) = -

        # store the cmd in string and then execute
        _to_exec = 'xrandr --output {0} --brightness {1:.2f}'.format(self.get_current_screen(), new_brightness)
        print(_to_exec)
        cmd_status = check_output(_to_exec, shell=True)

    def brightness_down(self):
        if float(self.get_current_brightness()) > 0.40:
            self.adjust_brightness(action='down')

    def brightness_up(self):
        if int(self.get_current_brightness()) < 1:
            self.adjust_brightness(action='up')


class WindowsVideoAdapter(GenericVideoAdapter):

    def get_current_screen(self):
        pass

    def get_current_brightness(self):
        pass

    def brightness_down(self):
        pass

    def brightness_up(self):
        pass


class MacVideoAdapter(GenericVideoAdapter):

    def get_current_screen(self):
        pass

    def get_current_brightness(self):
        pass

    def brightness_down(self):
        pass

    def brightness_up(self):
        pass


class VideoAdapter:

    _video_adapters = {
        'Linux': LinuxVideoAdapter,
        'Windows': WindowsVideoAdapter,
        'Darwin': MacVideoAdapter
    }

    def __init__(self):
        self.video_adapter = self.get_video_adapter()

    def get_video_adapter(self):
        video_adapter = self._video_adapters.get(platform.system())

        if video_adapter is not None:
            return video_adapter()
        else:
            raise Exception('Video Adapter is Invalid, system {}'.format(platform.system()))

    def process(self, action):
        return self.video_adapter.proccess(action)