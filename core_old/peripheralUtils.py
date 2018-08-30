__author__ = 'Lucas Navarro'
import platform
from subprocess import call, check_call
from pykeyboard import PyKeyboard


def keyboard_action(action):
    print('keyboard_action %s'%action)
    actions = {}

    if platform.system() == 'Linux':
        actions = {
            'change_window_start':  change_window_start,
            'change_window_finish': change_window_finish,
            'next_tab': next_tab,
            'previous_tab': previous_tab,
            'next_focus': next_focus,
            'previous_focus': previous_focus,
            'arrow_up': arrow_up,
            'arrow_down': arrow_down,
            'arrow_left': arrow_left,
            'arrow_right': arrow_right,
            'new_tab': new_tab,
            'close_tab': close_tab,

        }

    actions[action]()


def key_pressed(action):
    print('*_* key_pressed %s' % action)
    k = PyKeyboard()

    if action == 'enterKey':
        k.tap_key(k.enterkey)
    elif action == 'backSpace':
        k.tap_key(k.backspace_key)
    elif action == 'spaceKey':
        k.tap_key(k.space_key)
    else:
        k.tap_key('%s' % action)


def next_tab():

    print('*_* next_tab')
    k = PyKeyboard()

    k.press_key(k.control_l_key)
#    k.press_key(k.shift_key)
    k.tap_key(k.tab_key)

    k.release_key(k.control_l_key)
#    k.release_key(k.shift_key)


def previous_tab():

    print('*_* previous_tab')
    k = PyKeyboard()

    k.press_key(k.control_l_key)
    k.press_key(k.shift_key)
    k.tap_key(k.tab_key)

    k.release_key(k.control_l_key)
    k.release_key(k.shift_key)


def new_tab():
    print('*_* new_tab')
    k = PyKeyboard()
    k.release_key(k.control_l_key)

    k.press_key(k.control_l_key)
    k.tap_key('t')

    k.release_key(k.control_l_key)


def close_tab():
    print('*_* new_tab')
    k = PyKeyboard()
    k.release_key(k.control_l_key)

    k.press_key(k.control_l_key)
    k.tap_key(k.function_keys[4])F

    k.release_key(k.control_l_key)


def next_focus():

    print('*_* next_focus')
    k = PyKeyboard()
    k.tap_key(k.tab_key)


def previous_focus():

    print('*_* next_focus')
    k = PyKeyboard()
    k.press_key(k.shift_key)
    k.tap_key(k.tab_key)
    k.release_key(k.shift_key)


def change_window_start():

    print('*_* change_window_start')
    k = PyKeyboard()
    k.release_key(k.alt_key)
    k.press_key(k.alt_key)
    k.tap_key(k.tab_key)



def change_window_finish():

    print('*_* change_window_finish')
    k = PyKeyboard()
    k.release_key(k.alt_key)


def arrow_up():

    print('*_* arrow_up')
    k = PyKeyboard()
    k.tap_key(k.up_key)


def arrow_down():

    print('*_* arrow_down')
    k = PyKeyboard()
    k.tap_key(k.down_key)


def arrow_left():

    print('*_* arrow_left')
    k = PyKeyboard()
    k.tap_key(k.left_key)


def arrow_right():

    print('*_* arrow_right')
    k = PyKeyboard()
    k.tap_key(k.right_key)