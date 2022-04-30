import contextlib
import sys


@contextlib.contextmanager
def get_stream(stream, mode):
    """
    a context manager for files, which can be default standard input or output
    """
    if stream == sys.stdin:
        file = sys.stdin
    elif stream == sys.stdout:
        file = sys.stdout
    else:
        file = open(stream, mode)
    try:
        yield file
    finally:
        file.close()
