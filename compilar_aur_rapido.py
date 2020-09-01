import os
from time import sleep


def qual_gerenciador(gerenciador=''):
    file = open('/tmp/verificar.log', 'r')
    file.seek(0)
    if gerenciador in file.read():
        print(f'ok')
    else:
        sleep(5)
        print(f"{gerenciador} nâo instalado")
        print(f'preparando para instala {gerenciador}')
        os.system('sudo pacman -S --noconfirm ' + gerenciador)
    file.close()


def file_open(enter='Vazio', format=True):
    if format == True:
        file = open('/tmp/makepkg.conf', 'a+')
    else:
        file = open('/tmp/makepkg.conf', 'w+')
    file.write(enter)
    file.close()

def define_make(core='0'):
    if core == '0':
        file_open('MAKEFLAGS="-j$(($(nproc)+1))"')
    else:
        file_open(enter='MAKEFLAGS="-j'+ core, format=True)


def bakup_append():
    bkp = os.path.isfile('/etc/makepkg.conf.bkp')
    if bkp == False:
        os.system('sudo cp /tmp/makepkg.conf /etc/makepkg.conf.bkp')
        os.system('sudo cp /tmp/makepkg.conf /etc/makepkg.conf')
    else:
        os.system('sudo cp /tmp/makepkg.conf /etc/makepkg.conf')


def file_finally(core='0'):
    file_open(enter="""

# Other common tools:
# /usr/bin/snarf
# /usr/bin/lftpget -c
# /usr/bin/wget

#-- The package required by makepkg to download VCS sources
#  Format: 'protocol::package'
VCSCLIENTS=('bzr::bzr'
            'git::git'
            'hg::mercurial'
            'svn::subversion')

#########################################################################
# ARCHITECTURE, COMPILE FLAGS
#########################################################################
#
CARCH="x86_64"
CHOST="x86_64-pc-linux-gnu"

#-- Compiler and Linker Flags
CPPFLAGS="-D_FORTIFY_SOURCE=2"
CFLAGS="-march=native -O2 -pipe -fstack-protector-strong -fno-plt"
CXXFLAGS="${CFLAGS}"
LDFLAGS="-Wl,-O1,--sort-common,--as-needed,-z,relro,-z,now"
#RUSTFLAGS="-C opt-level=2"
#-- Make Flags: change this for DistCC/SMP systems 
""", format=True)


    define_make(core=core)


    file_open(""""
#-- Debugging flags
DEBUG_CFLAGS="-g -fvar-tracking-assignments"
DEBUG_CXXFLAGS="-g -fvar-tracking-assignments"
#DEBUG_RUSTFLAGS="-C debuginfo=2"

#########################################################################
# BUILD ENVIRONMENT
#########################################################################
#
# Defaults: BUILDENV=(!distcc !color !ccache check !sign)
#  A negated environment option will do the opposite of the comments below.
#
#-- distcc:   Use the Distributed C/C++/ObjC compiler
#-- color:    Colorize output messages
#-- ccache:   Use ccache to cache compilation
#-- check:    Run the check() function if present in the PKGBUILD
#-- sign:     Generate PGP signature file
#
BUILDENV=(!distcc color !ccache check !sign)
#
#-- If using DistCC, your MAKEFLAGS will also need modification. In addition,
#-- specify a space-delimited list of hosts running in the DistCC cluster.
#DISTCC_HOSTS=""
#
#-- Specify a directory for package building.
#BUILDDIR=/tmp/makepkg

#########################################################################
# GLOBAL PACKAGE OPTIONS
#   These are default values for the options=() settings
#########################################################################
#
# Default: OPTIONS=(!strip docs libtool staticlibs emptydirs !zipman !purge !debug)
#  A negated option will do the opposite of the comments below.
#
#-- strip:      Strip symbols from binaries/libraries
#-- docs:       Save doc directories specified by DOC_DIRS
#-- libtool:    Leave libtool (.la) files in packages
#-- staticlibs: Leave static library (.a) files in packages
#-- emptydirs:  Leave empty directories in packages
#-- zipman:     Compress manual (man and info) pages in MAN_DIRS with gzip
#-- purge:      Remove files specified by PURGE_TARGETS
#-- debug:      Add debugging flags as specified in DEBUG_* variables
#
OPTIONS=(strip docs !libtool !staticlibs emptydirs zipman purge !debug)

#-- File integrity checks to use. Valid: md5, sha1, sha224, sha256, sha384, sha512, b2
INTEGRITY_CHECK=(md5)
#-- Options to be used when stripping binaries. See `man strip' for details.
STRIP_BINARIES="--strip-all"
#-- Options to be used when stripping shared libraries. See `man strip' for details.
STRIP_SHARED="--strip-unneeded"
#-- Options to be used when stripping static libraries. See `man strip' for details.
STRIP_STATIC="--strip-debug"
#-- Manual (man and info) directories to compress (if zipman is specified)
MAN_DIRS=({usr{,/local}{,/share},opt/*}/{man,info})
#-- Doc directories to remove (if !docs is specified)
DOC_DIRS=(usr/{,local/}{,share/}{doc,gtk-doc} opt/*/{doc,gtk-doc})
#-- Files to be removed from all packages (if purge is specified)
PURGE_TARGETS=(usr/{,share}/info/dir .packlist *.pod)
#-- Directory to store source code in for debug packages
DBGSRCDIR="/usr/src/debug"

#########################################################################
# PACKAGE OUTPUT
#########################################################################
#
# Default: put built package and cached source in build directory
#
#-- Destination: specify a fixed directory where all packages will be placed
#PKGDEST=/home/packages
#-- Source cache: specify a fixed directory where source files will be cached
#SRCDEST=/home/sources
#-- Source packages: specify a fixed directory where all src packages will be placed
#SRCPKGDEST=/home/srcpackages
#-- Log files: specify a fixed directory where all log files will be placed
#LOGDEST=/home/makepkglogs
#-- Packager: name/email of the person or organization building packages
#PACKAGER="John Doe <john@doe.com>"
#-- Specify a key to use for package signing
#GPGKEY=""

#########################################################################
# COMPRESSION DEFAULTS
#########################################################################
#
COMPRESSGZ=(gzip -c -f -n)
COMPRESSBZ2=(bzip2 -c -f)
COMPRESSXZ=(xz -c -z -)
COMPRESSZST=(zstd -c -z -q -)
COMPRESSLRZ=(lrzip -q)
COMPRESSLZO=(lzop -q)
COMPRESSZ=(compress -c -f)
COMPRESSLZ4=(lz4 -q)
COMPRESSLZ=(lzip -c -f)

#########################################################################
# EXTENSION DEFAULTS
#########################################################################
#
PKGEXT='.pkg.tar.zst'
SRCEXT='.src.tar.gz' """, format=True)

    bakup_append()


file_open(enter="""#!/hint/bash
#
# /etc/makepkg.conf
#

#########################################################################
# SOURCE ACQUISITION
#########################################################################
#
#-- The download utilities that makepkg should use to acquire sources
#  Format: 'protocol::agent' 
""", format=False)


os.system('pacman -Q > /tmp/verificar.log && clear')
sleep(5)
print('=-' * 21)
print("""#          COMPILAR AUR RAPIDO           #
#                                        #
# ( 0 ) Padrão  ( 1 ) Axel  ( 2 ) Aria2  #""")
print('=-' * 21)

while True:
    option = int(input('Escolha um gerenciador de download: '))
    if option == 0:
        file_open(enter="""DLAGENTS=('file::/usr/bin/curl -gqC - -o %o %u'
              'ftp::/usr/bin/curl -gqfC - --ftp-pasv --retry 3 --retry-delay 3 -o %o %u'
              'http::/usr/bin/curl -gqb "" -fLC - --retry 3 --retry-delay 3 -o %o %u'
              'https::/usr/bin/curl -gqb "" -fLC - --retry 3 --retry-delay 3 -o %o %u'
              'rsync::/usr/bin/rsync --no-motd -z %u %o'
              'scp::/usr/bin/scp -C %u %o') """, format=True)
        print(f'Verificando se o gerenciador de download esta instalado...', end=" ")
        qual_gerenciador(gerenciador='curl')
        core = int(input("""====================================
Digite o numero de cores do seu processador. 
Se não sabe digite ( 0 ): """))
        c = core + 1
        cores = str(c)
        file_finally(core=cores)
        break

    elif option == 1:
        file_open(enter="""DLAGENTS=('file::/usr/bin/curl -gqC - -o %o %u'
              'ftp::/usr/bin/axel -n 5 -v -a -o %o %u'
              'http::/usr/bin/axel -n 5 -v -a -o %o %u'
              'https::/usr/bin/axel -n 5 -v -a -o %o %u'
              'rsync::/usr/bin/rsync --no-motd -z %u %o'
              'scp::/usr/bin/scp -C %u %o') """, format=True)
        print(f'Verificando se o gerenciador de download esta instalado...', end=" ")
        qual_gerenciador(gerenciador='axel')
        core = int(input("""====================================
Digite o numero de cores do seu processador. 
Se não sabe digite ( 0 ): """))
        c = core + 1
        cores = str(c)
        file_finally(core=cores)
        break

    elif option == 2:
        file_open(enter="""DLAGENTS=(file::/usr/bin/aria2c --allow-overwrite=true --continue=true --file-allocation=none --log-level=error --max-tries=10 --max-connection-per-server=10 --max-concurrent-downloads=5 --max-file-not-found=5 --min-split-size=5M --no-conf --remote-time=true --summary-interval=60 --timeout=5 --dir=/ --out %o %u
              ftp::/usr/bin/aria2c --allow-overwrite=true --continue=true --file-allocation=none --log-level=error --max-tries=10 --max-connection-per-server=10 --max-concurrent-downloads=5 --max-file-not-found=5 --min-split-size=5M --no-conf --remote-time=true --summary-interval=60 --timeout=5 --dir=/ --out %o %u
              http::/usr/bin/aria2c --allow-overwrite=true --continue=true --file-allocation=none --log-level=error --max-tries=10 --max-connection-per-server=10 --max-concurrent-downloads=5 --max-file-not-found=5 --min-split-size=5M --no-conf --remote-time=true --summary-interval=60 --timeout=5 --dir=/ --out %o %u
              https::/usr/bin/aria2c --allow-overwrite=true --continue=true --file-allocation=none --log-level=error --max-tries=10 --max-connection-per-server=10 --max-concurrent-downloads=5 --max-file-not-found=5 --min-split-size=5M --no-conf --remote-time=true --summary-interval=60 --timeout=5 --dir=/ --out %o %u
              rsync::/usr/bin/rsync --no-motd -z %u %o
              scp::/usr/bin/scp -C %u %o)""", format=True)
        print(f'Verificando se o gerenciador de download esta instalado...', end=" ")
        qual_gerenciador(gerenciador='aria2')
        core = int(input("""====================================
Digite o numero de cores do seu processador. 
Se não sabe digite ( 0 ): """))
        c = core + 1
        cores = str(c)
        file_finally(core=cores)
        break
    else:
        print('Opção INVALIDA')
