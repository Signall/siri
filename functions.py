from exec_functions import *
import datetime


def remind(matches: tuple, ords: tuple) -> tuple:
    """
    Remind me about ... in ... functionality.

    Possible inputs:

    i = item, t = time, u = units (hours mins etc)

     1. remind me about i in t u
     2. set a reminder for i in t u
     3. remind me in t u about i

    :param matches: tuple
    :param ords: tuple
    :return: tuple
    """

    i = t = u = None

    for match, ord in zip(matches, ords):
        if ord == 1:
            i = match
        elif ord == 2:
            t = match
        elif ord == 3:
            u = match

    return "I will remind you about {0} in {1} {2}".format(i, t, u), (start_timer, i, int(t), u)


def timer(matches: tuple, ords: tuple) -> tuple:
    """
    Set a timer for ... functionality.

    Possible inputs:

    t = time u = units

     1. set a timer for t u
     2. start a t u timer
     3. set a t u timer

    :param matches: tuple
    :param ords: tuple
    :return: tuple
    """

    t = u = None

    for match, ord in zip(matches, ords):
        if ord == 1:
            t = match
        elif ord == 2:
            u = match

    # [0] because it looks like [(t, u)].

    return "Setting a timer for {0} {1}".format(t, u), (start_timer, 'Done', int(t), u)


def web(matches: tuple, ords: tuple) -> tuple:
    """
    Search the web for ... functionality

    Possible inputs:

    s = search

     1. google s
     2. search the web for s

    :param matches: tuple
    :param ords: tuple
    :return: tuple
    """

    s = matches[0]
    # matches[0] because it's in the form (s, )

    return "Searching the web for {0}".format(s), (search_web, s)


def date(matches: tuple, ords: tuple) -> tuple:
    """
    Whats the date today? functionality.

    :param matches: tuple
    :param ords: tuple
    :return: tuple
    """