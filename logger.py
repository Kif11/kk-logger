import sys
import time
import datetime

class Logger(object):

    def __init__ (self, name='', debug=True, log_time=False, log_type=True, log_color=''):

        self._INFO = '[+]'
        self._WARNING = '[-]'
        self._ERROR = '[!]'
        self._DEBUG = '[D]'
        self._SEP_CHAR = '-'
        self._colors = {
            'green': '\033[0;32m\b\b\b\b\b\b\b\b',
            'red': '\033[0;31m',
            'yellow': '\033[0;33m',
            'light_grey': '\033[38;5;250m',
            'end': '\033[0m'
        }

        self.is_tty = sys.stdin.isatty() # True if running from a terminal

        self.name = name

        if self.is_tty:
            self.log_time = log_time
        else:
            self.log_time = True

        self.log_type = log_type
        self.log_color = log_color
        self.debug_active = debug

        if self.log_color:
            pass
        else:
            self.log_color = self._use_colors()

    def _use_colors(self):

        # Do not use collor if running not within a terminal
        if not self.is_tty:
            return False

        if sys.platform == 'darwin':
            return True
        elif sys.platform == 'win32':
            return False
        elif sys.platform == 'linux2':
            return False
        else:
            return False

    def make_msg(self, msg, msg_type = '', color=''):

        if color in self._colors.keys():
            color = self._colors[color]

        msg_body = ''
        for i in msg:
            msg_body = msg_body + '%s' % i

        cur_time = datetime.datetime.now().strftime('%H:%M:%S')
        msg = msg_body
        if self.log_time:
            msg = '%s - %s' % (cur_time, msg)
        if self.name:
            msg = '%s: %s' % (self.name, msg)
        if self.log_type:
            msg = '%s %s' % (msg_type, msg)
        if self.log_color:
            msg = '%s%s%s' % (color, msg, self._colors['end'])

        return msg

    def log(self, msg):
        print msg
        self.flush();

    def info(self, *args):
        msg = self.make_msg(args, self._INFO)
        self.log(msg)

    def warning(self, *args):
        msg = self.make_msg(args, self._WARNING, 'yellow')
        self.log(msg)

    def debug(self, *args):
        if self.debug_active:
            msg = self.make_msg(args, self._DEBUG, 'light_grey')
            self.log(msg)
        else:
            pass

    def error(self, *args):
        msg = self.make_msg(args, self._ERROR, 'red')
        self.log(msg)

    def success(self, *args):
        msg = self.make_msg(args, self._ERROR, 'green')
        self.log(msg)

    def line(self):
        """
        Print separation line of 80 chars.
        """
        self.log(self._SEP_CHAR * 80)

    def flush(self):
        sys.stdout.flush()
        sys.stderr.flush()
