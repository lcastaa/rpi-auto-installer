import os
from pathlib import Path


class FirewallConfig:

    def __init__(self):
        pass

    def addrule(self):
        os.chdir('/bin')
        path_to_file = 'ufw'
        path = Path(path_to_file)
        if path.is_file():
            firewallrules = []
            i = 1
            limit = int(input('How many rules you have?: '))
            while i != limit:
                count = 1
                rule = int(input('Enter Rule #' + count + ': '))
                firewallrules.append(rule)
                count += 1
                i += 1
            o = 0
            while o != limit:
                for rule in firewallrules:
                    os.system('sudo ufw allow ' + rule)
        else:
            print('')
            print('UFW Doesnt Exist on system.....')
            print('')
            print('Installing Now....')
            os.system('sudo apt install ufw -y')
            self.addrule()
