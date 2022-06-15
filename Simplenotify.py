# We need modules like time and notifier or something  like that
import time
from plyer import notification


def function():
        notification.notify(
            title = "Python notifier",
            message = "The programme is working nice!!",
            timeout = 5
    )
        time.sleep(2)

f = function()
