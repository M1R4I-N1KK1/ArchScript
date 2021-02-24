import os
import backup_restore
import subprocess as sub


def apply_backup(confirm):
    while True:
        if os.path.exists('/etc/makepkg.conf.bk'):
            if confirm == 'y':
                sub.call(['sudo', 'mv', 'new_make_core.conf', '/etc/makepkg.conf'])
                print('successfully applied')
                break
            else:
                print('configuration not applied')
                break
        else:
            backup_restore.backup()
