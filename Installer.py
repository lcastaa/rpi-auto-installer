import os
import time


class Installer:

    UPDATEPI = 'sudo apt-get update && sudo apt-get full-upgrade -y'
    PIHOLECMD = 'sudo curl -sSL https://install.pi-hole.net | sudo bash'
    PIVPNCMD = 'sudo curl -L https://install.pivpn.io | sudo bash'
    DOCKERCMD = 'sudo curl -sSL https://get.docker.com | sudo sh'
    OMV6CMD = 'sudo wget -O - https://github.com/OpenMediaVault-Plugin-Developers/installScript/raw/master/install | ' \
              'sudo bash'
    APACHE2CMD = 'sudo apt install apache2 -y'
    NGINXCMD = 'sudo apt install nginx -y'
    HOMEBRIDGECMD = 'sudo apt-get install homebridge -y'
    PIP3CMD = 'sudo apt-get install python3-pip -y'
    PIPDEPENDECIES = ['sudo pip3 install --upgrade setuptools', 'sudo pip3 install --upgrade adafruit-python-shell', 'sudo pip3 install adafruit-circuitpython-ssd1306']
    RASPIBLINKACMD = 'sudo wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master' \
                     '/raspi-blinka.py'
    PIL3CMD = 'sudo apt-get install python3-pil -y'
    GITCMD = 'sudo apt install git -y'
    OLEDSTATS = 'git clone https://github.com/mklements/OLED_Stats.git'

    def __init__(self):
        pass

    def installer(self):

        print('')
        print('Enter App to install:')
        print('-- [1] Pi-Hole --')
        print('-- [2] Pi-Vpn --')
        print('-- [3] Docker --')
        print('-- [4] Open-Media-Vault 6 --')
        print('-- [5] Apache-2 --')
        print('-- [6] Nginx --')
        print('-- [7] Home-Bridge --')
        print('-- [8] I2C-Display-Configure --')
        choice = int(input('Choice ->: '))

        if choice == 1:
            print()
            print('Installing Pi-Hole...')
            print()
            time.sleep(1.5)
            os.system(self.PIHOLECMD)
            self.installer()

        elif choice == 2:
            print()
            print('Installing Pi-VPN...')
            print()
            time.sleep(1.5)
            os.system(self.PIVPNCMD)
            self.installer()

        elif choice == 3:
            print()
            print('Updating Raspberry Pi....')
            time.sleep(1.5)
            os.system(self.UPDATEPI)
            print()
            print('Installing Docker...')
            time.sleep(1.5)
            os.system(self.DOCKERCMD)
            print()
            print('Adding user to docker group...')
            os.system('sudo usermod -aG docker [user_name]')
            self.installer()

        elif choice == 4:
            print()
            print('Installing OpenMediaVault 6....')
            print()
            time.sleep(1.5)
            os.system(self.OMV6CMD)
            self.installer()

        elif choice == 5:
            print()
            print('Installing Apache2...')
            print()
            time.sleep(1.5)
            os.system(self.APACHE2CMD)

        elif choice == 6:
            print()
            print('Installing Nginx...')
            print()
            time.sleep(1.5)
            os.system(self.NGINXCMD)
            self.installer()

        elif choice == 7:
            time.sleep(1.5)
            print()
            print('Installing GPG key...')
            os.system('sudo curl -sSfL https://repo.homebridge.io/KEY.gpg | sudo gpg --dearmor | sudo tee '
                      '/usr/share/keyrings/homebridge.gpg  > /dev/null && echo "deb ['
                      'signed-by=/usr/share/keyrings/homebridge.gpg] https://repo.homebridge.io stable main" | sudo '
                      'tee /etc/apt/sources.list.d/homebridge.list > /dev/null')
            time.sleep(1.5)
            print()
            print('Updating Pi...')
            os.system(self.UPDATEPI)
            time.sleep(1.5)
            print()
            print('Installing Home-Bridge...')
            os.system(self.HOMEBRIDGECMD)
            self.installer()

        elif choice == 8:
            print()
            print('Installing IC2 Dependencies...')
            os.system(self.UPDATEPI)
            time.sleep(1.5)
            os.system(self.PIP3CMD)
            print('Installing PIP dependencies...')
            time.sleep(1.5)
            for dependency in self.PIPDEPENDECIES:
                os.system(dependency)
            time.sleep(1.5)
            print()
            print('Downloading Raspi-Blinka...')
            os.system(self.RASPIBLINKACMD)
            time.sleep(1.5)
            print()
            print('Installing Python PIL...')
            os.system(self.PIL3CMD)
            time.sleep(1.5)
            print()
            print('Installing Git...')
            os.system(self.GITCMD)
            time.sleep(1.5)
            print()
            print('Cloning Stats Script...')
            os.system(self.OLEDSTATS)
            time.sleep(1.5)
            print()
            print('Starting Raspi-blinka ...')
            os.system('sudo python3 raspi-blinka.py')

        else:
            print('')
            print('Wrong choice try again')
            print('')
            self.installer()
