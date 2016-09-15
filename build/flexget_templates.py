import os
import re
import locale
import jinja2
from copy import copy
from datetime import datetime, date, time
from email.utils import parsedate
from time import mktime

def filter_pathbase(val):
    """Base name of a path."""
    return os.path.basename(val or '')

def filter_pathname(val):
    """Base name of a path, without its extension."""
    return os.path.splitext(os.path.basename(val or ''))[0]

def filter_pathext(val):
    """Extension of a path (including the '.')."""
    return os.path.splitext(val or '')[1]

def filter_pathdir(val):
    """Directory containing the given path."""
    return os.path.dirname(val or '')

def filter_pathscrub(val, os_mode=None):
    """Replace problematic characters in a path."""
    return pathscrub(val, os_mode)

def filter_re_replace(val, pattern, repl):
    """Perform a regexp replacement on the given string."""
    return re.sub(pattern, repl, str(val))

def filter_re_search(val, pattern):
    """Perform a search for given regexp pattern, return the matching portion of the text."""
    if not isinstance(val, basestring):
        return val
    result = re.search(pattern, val)
    if result:
        return result.group(0)
    return ''

def filter_formatdate(val, format):
    """Returns a string representation of a datetime object according to format string."""
    encoding = locale.getpreferredencoding()
    if not isinstance(val, (datetime, date, time)):
        return val
    return val.strftime(format.encode(encoding)).decode(encoding)

def filter_parsedate(val):
    """Attempts to parse a date according to the rules in RFC 2822"""
    return datetime.fromtimestamp(mktime(parsedate(val)))

def filter_date_suffix(date):
    day = int(date[-2:])
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    return date + suffix

def filter_format_number(val, places=None, grouping=True):
    """Formats a number according to the user's locale."""
    if not isinstance(val, (int, float, int)):
        return val
    if places is not None:
        format = '%.' + str(places) + 'f'
    elif isinstance(val, (int, int)):
        format = '%d'
    else:
        format = '%.02f'

    locale.setlocale(locale.LC_ALL, '')
    return locale.format(format, val, grouping)

def filter_pad(val, width, fillchar='0'):
    """Pads a number or string with fillchar to the specified width."""
    return str(val).rjust(width, fillchar)

def filter_to_date(date_time_val):
    if not isinstance(date_time_val, (datetime, date, time)):
        return date_time_val
    return date_time_val.date()


# Override the built-in Jinja default filter to change the `boolean` param to True by default
def filter_default(value, default_value='', boolean=True):
    return jinja2.filters.do_default(value, default_value, boolean)

filter_d = filter_default