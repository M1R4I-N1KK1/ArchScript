import subprocess
import os
import sys


def value():
    return float(os.popen("xrandr --verbose --current | grep VGA1 -A5 | tail -n1").read()[13:])


def up_down(argv):
    if argv in '-inc':
        if 0.90 > value():
            return str(float(value()) + 0.10)
        else:
            return '0.90'

    elif argv in '-dec':
        if 0.40 < value():
            return str(float(value()) - 0.10)
        else:
            return '0.40'


arg = str(sys.argv[1:])[2:][:4]
if arg in ['-inc', '-dec']:
    subprocess.run(["xrandr", "--output", "VGA1", "--brightness", up_down(arg)])
else:
    print("""
usage: xbrightness [-inc]   increase brightness
                   [-dec]   decrease brightness
                   [--help] help
    """)
