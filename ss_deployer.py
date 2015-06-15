#!/usr/bin/env python

from optparse import OptionParser
import os, sys

pkg_manger = ""
rc_manager = ""


# generate a colored-term

try:
    from termcolor import colored
except:
    ATTRIBUTES = dict( list(zip([ 'bold', 'dark', '', 'underline', 'blink', '', 'reverse', 'concealed' ], list(range(1, 9)))))
    del ATTRIBUTES['']
    HIGHLIGHTS = dict( list(zip([ 'on_grey', 'on_red', 'on_green', 'on_yellow', 'on_blue', 'on_magenta', 'on_cyan', 'on_white' ], list(range(40, 48)))))
    COLORS = dict(list(zip(['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', ], list(range(30, 38)))))
    RESET = '\033[0m'

    def colored(text, color=None, on_color=None, attrs=None):
        fmt_str = '\033[%dm%s'
        if color is not None: text = fmt_str % (COLORS[color], text)
        if on_color is not None: text = fmt_str % (HIGHLIGHTS[on_color], text)
        if attrs is not None:
            for attr in attrs:
                text = fmt_str % (ATTRIBUTES[attr], text)

        text += RESET
        return text

def check_system():
    global pkg_manger, rc_manager

    if os.system('apt-get') >> 8 == 0:
        pkg_manager = 'apt-get'
    elif os.system('yum') >> 8 == 0:
        pkg_manager = 'yum'
    else:
        print colored('[*] No pkg-manager found!', 'red')
        sys.exit(1)

    print colored('[*] Detected %s' % pkg_manager, 'green')

    if os.system('chkconfig') >> 8 == 0:
        rc_manager = 'chkconfig'
    elif os.system('update-rc.d') >> 8 == 0:
        rc_manager = 'update-rc.d'
    else:
        print '[*] No rc-manager found!'
        sys.exit(1)

    print colored('[*] Detected %s' % rc_manager, 'green')

if __name__ == '__main__':
    check_system()