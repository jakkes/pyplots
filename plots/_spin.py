import threading


def spin(cancellation_event: threading.Event=None):
    """Sets the current thread into a spin, keeping the it alive for any plots to remain
    open.

    Args:
        cancellation_event (threading.Event, optional): If given, the spin is interupted
            whenever the event is set.
    """

    if cancellation_event is None:
        cancellation_event = threading.Event()

    while not cancellation_event.wait(1.0):
        pass
