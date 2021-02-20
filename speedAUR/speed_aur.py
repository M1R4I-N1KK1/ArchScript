import json
import window
from os import path, system


def clear():
    system('clear')


directory = path.dirname(__file__)
dl = ['curl', 'axel', 'aria2']

with open(directory + '/manager.json') as dm:
    manager = json.load(dm)

with open(directory + '/base', 'r') as file:
    f = file.read()

while True:
    window.window_manager()
    option = input('choose an option: ')
    if option == '0' or option == '1' or option == '2':
        dl = dl[int(option)]
        break

while True:
    window.window_core()
    option_core = int(input('choose an option: '))
    if option_core == 0:
        option_core = 2
        break
    break
new_make = f.replace('MANAGER', str(manager[dl][0]))
new_make_core = new_make.replace('CORE', str(option_core + 1))

with open(directory + '/new_make.conf', 'w+') as make:
    make.write(new_make_core)
