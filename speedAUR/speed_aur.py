import json
import window
from os import path

directory = path.dirname(__file__)
dl = 'curl'

with open(directory + '/manager.json') as dm:
    manager = json.load(dm)

with open(directory + '/base', 'r') as file:
    f = file.read()

window.window_manager()
option = int(input('choose an option: '))
if option == 0:
    dl = 'curl'
if option == 1:
    dl = 'axel'
if option == 2:
    dl = 'aria2'

new_make = f.replace('MANAGER', str(manager[dl][0]))

with open(directory + '/new_make.conf', 'w+') as make:
    make.write(new_make)
