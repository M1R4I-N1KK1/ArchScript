import subprocess as sub


def backup():
    sub.call(['sudo', 'cp', '/etc/makepkg.conf', '/etc/makepkg.conf.bk'])


def restore():
    sub.call(['sudo', 'cp', '/etc/makepkg.conf.bk', '/etc/makepkg.conf'])
