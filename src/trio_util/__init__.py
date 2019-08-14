from ._version import __version__
from ._async_bool import AsyncBool
from ._async_dictionary import AsyncDictionary
from ._async_itertools import azip, azip_longest
from ._async_value import AsyncValue
from ._awaitables import wait_all, wait_any
from ._exceptions import defer_to_cancelled
from ._periodic import periodic
from ._repeated_event import UnqueuedRepeatedEvent, MailboxRepeatedEvent
from ._task_stats import TaskStats

def _metadata_fix():
    # don't do this for Sphinx case because it breaks "bysource" member ordering
    import sys
    if 'sphinx' in sys.modules:
        return

    for name, value in globals().items():
        if not name.startswith('_'):
            value.__module__ = __name__

_metadata_fix()
