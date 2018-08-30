# -*- coding : utf-8 -*-
__author__ = 'Lucas Navarro'
import platform
from subprocess import call, check_call
from abc import ABC, abstractmethod


class GenericSoundMixer(ABC):

    def __init__(self, ):
        self.mapped_actions = {
            'vu': self.volume_up,
            'vd': self.volume_down,
            'vm': self.volume_mute,
            'vt': self.volume_unmute
        }
        super().__init__()

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

    @abstractmethod
    def volume_mute(self):
        pass

    @abstractmethod
    def volume_unmute(self):
        pass

    def process(self, action):
        _action = self.mapped_actions.get(action)

        if _action is not None:
            return _action()
        else:
            raise Exception('Action {} is not defined in Generic Sound Mixer'.format(action))


class LinuxSoundMixer(GenericSoundMixer):

    def volume_down(self):
        check_call(["amixer", "sset", "Master", "10%-"])

    def volume_up(self):
        check_call(["amixer", "sset", "Master", "10%+"])

    def volume_mute(self):
        check_call(["amixer", "sset", "Master", "0%"])

    def volume_unmute(self):
        check_call(["amixer", "sset", "Master", "50%"])


class WindowsSoundMixer(GenericSoundMixer):

    def volume_down(self):  # TODO
        pass

    def volume_up(self):    # TODO
        pass

    def volume_mute(self):
        pass

    def volume_unmute(self):
        pass


class MacSoundMixer(GenericSoundMixer):

    def volume_down(self):  # TODO
        pass

    def volume_up(self):    # TODO
        pass

    def volume_mute(self):
        pass

    def volume_unmute(self):
        pass


class SoundMixer:

    _sound_mixers = {
        'Linux': LinuxSoundMixer,
        'Windows': WindowsSoundMixer,
        'Darwin': MacSoundMixer
    }

    def __init__(self):
        self.mixer = self.get_sound_mixer()

    def get_sound_mixer(self):
        sound_mixer = self._sound_mixers.get(platform.system())

        if sound_mixer is not None:
            return sound_mixer()
        else:
            raise Exception('Sound Mixer is Invalid, system {}'.format(platform.system()))

    def process(self, action):
        return self.mixer.process(action)
