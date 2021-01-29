"""
This scripts creates two unique colours for each day of the year.
A background (bg) and font color. The font is based on an inverted
hue from the bg. Colours are delivered as hex values.
"""

import colorsys
from datetime import datetime
from calendar import monthrange


def create():

    now = datetime.now()

    sv = int(now.month * (100 / 12))
    h = int(now.day * (360 / monthrange(now.year, now.month)[-1]))
    h = 359 if h == 360 else h

    hex_values = {
        'bg': _hsv_to_hex(h, sv),
        'font': _hsv_to_hex(_invert(h), sv)
    }

    return hex_values


def _hsv_to_hex(h, sv):
    gb = sv / 100
    rgb = [round(x*255) for x in colorsys.hsv_to_rgb(h / 360, gb, gb)]
    return '%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])


def _hsv_test():
    val = 100 / 12
    for month in range(1, 13):
        y = z = int(month * val)
        for day in range(1, 32):
            x = int(day * 11.612903225806452)
            x = 359 if x == 360 else x
            hsv = [x, y, z]
            print(hsv)


def _invert(x):
    return int(x + 179 if x < 179 else x - 179)


def _main():
    colours = create()
    for each in colours:
        print("{}: {}".format(each, colours[each]))


if __name__ == '__main__':
    _main()