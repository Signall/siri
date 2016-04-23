import time
import winsound as ws
import webbrowser as wb

SECONDS_IN_YEAR = 31104000
SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


def start_timer(i, t, u):
    """
    Takes output from functions.remind() or functions.timer() and starts the timer

    :param i: str
    :param t: int
    :param u: str
    :return:
    """

    units = {
        "years": t * SECONDS_IN_YEAR,
        "year": t * SECONDS_IN_YEAR,
        "days": t * SECONDS_IN_DAY,
        "day": t * SECONDS_IN_DAY,
        "hours": t * SECONDS_IN_HOUR,
        "hour": t * SECONDS_IN_HOUR,
        "minutes": t * SECONDS_IN_MINUTE,
        "minute": t * SECONDS_IN_MINUTE,
        "seconds": t,
        "second": t
    }

    try:
        seconds = units[u]
    except KeyError:
        return "Time must be in years, days, hours, minutes, or seconds. Bad unit was {}".format(u)

    time.sleep(seconds)
    if i:
        # If the call came from the functions.remind() it will have an i or item,
        # else if it came from functions.timer(), do nothing.
        print(i)

    ws.PlaySound('radar.wav', ws.SND_FILENAME)


def search_web(s):
    """
    Takes output from functions.web() and opens browser window.

    :param s: str
    :return:
    """

    # Webbrowser stuff

    new = 2  # Open a new tab if possible in existing window

    # Turn string into google url.

    url = 'https://www.google.com/webhp?#q=' + s.replace(' ', '+')

    wb.open(url, new)


def null(nothing):
    """
    For tasks that don't require another function.

    :return: None
    """
    pass







