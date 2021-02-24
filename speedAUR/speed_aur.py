import json
import window
import final_process
import backup_restore
import sys
from os import path, system


def resource_path(relative_path):
    return path.realpath(relative_path)


def clear():
    system('clear')


if '-r' in sys.argv:
    backup_restore.restore()
    print('backup restored.')

else:
    try:
        with open(resource_path('manager.json')) as download_manager:
            manager = json.load(download_manager)

        with open(resource_path('base.conf'), 'r') as base:
            base_make = base.read()

        while True:
            window.window_manager()
            option = input('choose an option: ')
            if option == '0' or option == '1' or option == '2':
                dl = option
                clear()
                break

        while True:
            window.window_core()
            option_core = int(input('choose an option: '))
            if option_core == 0:
                option_core = 2
                break
            break

        new_make = base_make.replace('MANAGER', str(manager[dl][0])).replace('CORE', str(option_core + 1))

        with open(resource_path('new_make_core.conf'), 'w+') as make:
            make.write(new_make)

        confirm = str(input('apply settings [Y/n]: '))
        final_process.apply_backup(confirm)

    except KeyboardInterrupt:
        print('\nGoodbye!!!')
