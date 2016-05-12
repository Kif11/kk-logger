import sys
import time
import datetime

class Logger(object):

    def __init__ (self, name='', debug=True, log_time=False, log_type=True):

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
        self.name = name
        self.log_time = log_time
        self.log_type = log_type

        self.debug_active = debug

    def make_msg(self, msg, msg_type = '', color=''):

        if color in self._colors.keys():
            color = self._colors[color]

        cur_time = datetime.datetime.now().strftime('%H:%M:%S')
        if self.log_time:
            msg = '%s %s' %(cur_time, msg)
        if self.name:
            msg = '%s: %s' %(self.name, msg)
        if self.log_type:
            msg = '%s%s %s%s' %(color, msg_type, msg, self._colors['end'])

        return msg

    def log(self, msg):
        print msg
        self.flush();

    def info(self, msg, *args):
        msg = self.make_msg(
            str(msg) + ''.join(args), self._INFO
        )
        self.log(msg)

    def warning(self, msg, *args):
        msg = self.make_msg(str(msg) + ''.join(args),
            self._WARNING,
            color='yellow'
        )
        self.log(msg)

    def debug(self, msg, *args):
        if (self.debug_active):
            msg = self.make_msg(
                str(msg) + ''.join(args),
                self._DEBUG,
                color='light_grey'
            )
            self.log(msg)
        else:
            pass

    def error(self, msg, *args):
        msg = self.make_msg(
            str(msg) + ''.join(args),
            self._ERROR,
            color='red'
        )
        self.log(msg)

    def success(self, msg, *args):
        msg = self.make_msg(
            str(msg) + ''.join(args),
            self._ERROR,
            color='green'
        )
        self.log(msg)

    def line(self):
        """
        Print separation line on 80 chars.
        """
        self.log(self._SEP_CHAR * 80)

    def flush(self):
        sys.stdout.flush()
        sys.stderr.flush()
