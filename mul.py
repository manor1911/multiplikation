#!/usr/bin/env python3

import argparse
import contextlib
import datetime
import itertools
import random
import time

low = 1
high = 10



def do_test():
    full_range = lambda: range(low, high + 1)
    test = list((l, h) for l, h in itertools.product(full_range(), full_range()))
    random.shuffle(test)

    now = time.monotonic()
    correct = 0
    wrong = 0
    wrongs = []

    try:
        for item in test:
            a, b = item
            question = '{} ∙ {} = '.format(a, b)
            answer = input(question)

            with contextlib.suppress(Exception):
                if int(answer) == a * b:
                    correct += 1
                    continue
            wrong += 1
            wrongs.append((item, answer))
    finally:
        total_time = time.monotonic() - now
        mins = int(total_time // 60)
        seconds = total_time - 60 * mins

    print('Antal rätt: {:2}'.format(correct))
    print('Antal fel:  {:2}'.format(wrong))
    print('Din tid: {} minut(er) och {} s'.format(mins, round(seconds)))
    if wrongs:
        print('Du hade fel på:')
        for (a, b), answer in wrongs:
            print('{} ∙ {}, ditt svar: {}, rätt svar: {}'.format(a, b, answer, a * b))

keep_running = True

def menu_quit():
    global keep_running
    keep_running = False

def set_limits():
    global low, high
    with contextlib.suppress(Exception):
        low = int(input('Ange nytt från värde: '))
        high = int(input('Ange nytt till värde: '))

menu_choices = [
    ('Kör test ({low} - {high})', do_test),
    ('Ändra gränser', set_limits),
    ('Avsluta', menu_quit)
]

def menu():
    for num, choice in enumerate(menu_choices, 1):
        print(str(num), choice[0].format(**globals()))

    fun = lambda: None # Do nothing

    with contextlib.suppress(Exception):
        index = int(input('Välj: ')) - 1
        fun = menu_choices[index][1]

    fun()

while keep_running:
    menu()
