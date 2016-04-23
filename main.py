from functions import *
from exec_functions import *
import re

input_ = "start a 2 second timer"

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
         (re.compile(u'search the web for (.+)', re.I), (1))]
}


def main(string):

    for function, options in all_options.items():

            match = [(re.match(option, string), order) for option, order in options if re.match(option, string)]

            if not match:
                continue

            match = match[0]
            # match[0] because of the [()]

            match = match[0].groups(), match[1]

            out = function(*match)
            print(out[0])
            out[1][0](*out[1][1:])




main(input_)
