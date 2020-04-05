#!/usr/bin/env python3
''' Script to write to a Pimoroni MicroDot pHAT '''

import argparse
import textwrap
import microdotphat as md


def update_display(cost, trend):
    ''' Function to update the display '''
    if (len(cost) > 1) and (len(cost) < 7):
        # Start with a clear buffer
        md.clear()

        # Right justify string
        char_offset = 6 - len(cost)
        md.write_string(cost, offset_x=(8 * char_offset), kerning=False)

        # Add trend - character set here: https://github.com/pimoroni/microdot-phat/blob/master/library/microdotphat/font.py
        if trend == 'UP':
            # Solid upwards triangle
            md.write_char(chr(9650), offset_x=0)
        elif trend == 'up':
            # Open upwards triangle
            md.write_char(chr(9651), offset_x=0)
        elif trend == 'down':
            # Open downwards triangle
            md.write_char(chr(9661), offset_x=0)
        elif trend == 'DOWN':
            # Solid downwards triangle
            md.write_char(chr(9660), offset_x=0)

        # Write the buffer to the display
        md.show()


PARSER = argparse.ArgumentParser(description=textwrap.dedent('''\
    Script to drive a Pimoroni MicroDot pHAT display'''), \
    formatter_class=argparse.RawTextHelpFormatter)

# cost
PARSER.add_argument('--cost',
                    dest='cost',
                    metavar='<cost in pence>',
                    help='The cost in pence (recommended to 1 decimal place)')

# Optional trend
PARSER.add_argument('--trend',
                    dest='trend',
                    choices=['UP', 'up', 'down', 'DOWN'],
                    help='The optional cost trend - case determines strength',
                    default='flat')

# Optional display brightness
PARSER.add_argument('--brightness',
                    dest='brightness',
                    metavar='<0.0 - 1.0>',
                    help='The display brightness to set, in range 0.0..1.0',
                    type=float)

# Optionally clear the display - this takes precedence
PARSER.add_argument('--clear',
                    dest='clear',
                    action='store_true',
                    help='Clear the display - takes precedence over other options')

ARGS = PARSER.parse_args()

if ARGS.clear:
    md.set_clear_on_exit(True)
else:
    if ARGS.brightness:
        md.set_brightness(ARGS.brightness)

    if ARGS.cost:
        update_display(ARGS.cost, ARGS.trend)

    md.set_clear_on_exit(False)
