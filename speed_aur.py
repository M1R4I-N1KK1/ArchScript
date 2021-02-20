import json
import window
from os import path, system


def resource_path(relative_path):
    return path.realpath(relative_path)


def clear():
    system('clear')


try:
    dl = ['curl', 'axel', 'aria2']
    base_json = str()
    with open(resource_path('manager.json')) as download_manager:
        manager = json.load(download_manager)

    with open(resource_path('base.conf'), 'r') as base:
        base_make = base.read()

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
    new_make = base_make.replace('MANAGER', str(manager[dl][0]))
    new_make_core = new_make.replace('CORE', str(option_core + 1))

    with open(resource_path('new_make_core.conf'), 'w+') as make:
        make.write(new_make_core)
except KeyboardInterrupt:
    print('Goodbye!')