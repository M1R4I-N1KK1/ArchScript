import json
import window
from os import path, system

directory = path.dirname(__file__)
dl = ['curl', 'axel', 'aria2']
core = 2

with open(directory + '/manager.json') as dm:
    manager = json.load(dm)

with open(directory + '/base', 'r') as file:
    f = file.read()

while True:
    system('clear')
    window.window_manager()
    option = int(input('choose an option: '))
    if option == 0 or option == 1 or option == 2:
        dl = dl[option]
        break

window.window_core()
option_core = int(input('choose an option: '))
new_make = f.replace('MANAGER', str(manager[dl][0]))
new_make_core = new_make.replace('CORE', str(option_core))

with open(directory + '/new_make.conf', 'w+') as make:
    make.write(new_make_core)
