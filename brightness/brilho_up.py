import subprocess
import os


def value():
    return os.popen("xrandr --verbose --current | grep VGA1 -A5 | tail -n1").read()[13:]


if '0.90' > value():
    subprocess.check_output(["xrandr", "--output", "VGA1", "--brightness", str(float(value()) + 0.10)])
