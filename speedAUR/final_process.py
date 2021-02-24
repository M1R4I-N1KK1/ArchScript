import subprocess as sub


def apply_backup(confirm):
    if confirm == 'y':
        sub.call(['sudo', 'mv', 'new_make_core.conf', '/etc/makepkg.conf'])
        print('successfully applied')
    else:
        print('configuration not applied')
