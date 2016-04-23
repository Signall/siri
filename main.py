from functions import *
from exec_functions import *
import re
import logging

# Start logging setup

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

dh = logging.FileHandler('debug.log')
dh.setLevel(logging.DEBUG)

eh = logging.FileHandler('error.log')
eh.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
dh.setFormatter(formatter)
eh.setFormatter(formatter)

logger.addHandler(dh)
logger.addHandler(eh)

# End logging setup

input_ = "whats the date today"
logger.debug("Input was: {0}".format(input_))

FUNCTIONS = [remind, timer, web]

all_options = {
    remind:
        [(re.compile(u'remind me about (.+) in ([0-9]+) (\w+)', re.I), (1, 2, 3)),
         (re.compile(u'set a reminder for (.+) in ([0-9]+) (\w+)', re.I), (1, 2, 3)),
         (re.compile(u'remind me in ([0-9]+) (\w+) about (.+)', re.I), (2, 3, 1))],
    timer:
        [(re.compile(u'start a timer for ([0-9]+) (\w+)', re.I), (1, 2)),
         (re.compile(u'start a ([0-9]+) (\w+) timer', re.I), (1, 2)),
         (re.compile(u'set a ([0-9]+) (\w+) timer', re.I), (1, 2))],
    web:
        [(re.compile(u'google (.+)', re.I), (1)),
         (re.compile(u'search the web for (.+)', re.I), (1))],
    date:
        [(re.compile(u'date', re.I), (0)),]
}


def main(string):

    for function, options in all_options.items():

            match = [(re.match(option, string), order) for option, order in options if re.match(option, string)]
            logger.debug("Match is {0}".format(match))

            if not match:
                continue

            logger.debug("There was a match!")

            match = match[0]
            logger.debug("match[0] = {0}".format(match))

            # match[0] because of the [()]

            match = match[0].groups(), match[1]

            out = function(*match)
            logger.debug("out = {0}".format(out))

            print(out[0])
            out[1][0](*out[1][1:])
            logger.info("Done!")


try:
    main(input_)
except Exception as e:
    logger.error(e)
