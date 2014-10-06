__author__ = 'Lucas Navarro'
import platform
from subprocess import call, check_call


def audio_action(action):
    print 'audioAction %s'%action
    actions = {}

    if platform.system() == 'Linux':
        actions = {
            'volume_up':  linux_volume_up,
            'volume_down': linux_volume_down,
        }

    actions[action]()


def linux_volume_up():
    print '*_* linux_volume_up'
    check_call(["amixer", "sset", "Master", "10%+"])


def linux_volume_down():
    print '*_* linux_volume_down'
    check_call(["amixer", "sset", "Master", "10%-"])


