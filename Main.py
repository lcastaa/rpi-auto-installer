import subprocess as sub
from Installer import Installer
from HostNameConfig import HostNameConfig
from Overclocker import Overclocker
from FirewallConfig import FirewallConfig
from sys import platform
from os.path import exists
from pathlib import Path


# Developed by Luis Castaneda (lcastaa)
def main():
    print('')
    print('Choose to execute')
    print('')
    print('[1] - Installer')
    print('[2] - Hostname Editor')
    print('[3] - OverClocker')
    print('[4] - FireWall Configurator')
    print('[5] - Auto Run..')
    print('')
    choice = int(input('Choice ->: '))
    if choice == 1:
        installer = Installer()
        installer.installer()
    elif choice == 2:
        hostnameconfig = HostNameConfig()
        hostnameconfig.change()
    elif choice == 3:
        overclocker = Overclocker()
        overclocker.overclock()
    elif choice == 4:
        firewallconfig = FirewallConfig()
        firewallconfig.addrule()


main()
