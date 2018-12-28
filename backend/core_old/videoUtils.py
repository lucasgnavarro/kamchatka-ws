from platform import platform

__author__ = 'Lucas Navarro'
import platform
from subprocess import call, check_call, check_output

brightness_scale = 10


def video_action(action):
    print("video_action %s"%action)
    actions = {}

    if platform.system() == 'Linux':
        actions = {
            'brightness_up': linux_brightness_up,
            'brightness_down': linux_brightness_down,
        }

    actions[action]()


def linux_brightness_up():

    print('*_* linux_brightness_up ')
    if int(get_current_brightness
               ()) == 1:
        return

    new_brightness = get_current_brightness() + (float(brightness_scale)/100)
    cmd = "xrandr --output %s --brightness %.2f" % (get_current_monitor(), new_brightness)
    cmd_status = check_output(cmd, shell=True)


def linux_brightness_down():

    print('*_* linux_brightness_down ')

    if float(get_current_brightness()) == 0.40:
        return

    new_brightness = get_current_brightness() - (float(brightness_scale)/100)
    cmd = "xrandr --output %s --brightness %.2f" % (get_current_monitor(), new_brightness)
    cmd_status = check_output(cmd, shell=True)


def get_current_brightness():
    if platform.system() == 'Linux':
        return float(check_output("xrandr --verbose | grep -i brightness | cut -f2 -d ' '", shell=True).strip())


def get_current_monitor():
    if platform.system() == 'Linux':
        return check_output("xrandr -q | grep ' connected' | cut -d ' ' -f1", shell=True).strip().decode('utf-8')