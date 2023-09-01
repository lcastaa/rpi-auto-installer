class HostNameConfig:

    def __init__(self):
        pass

    @staticmethod
    def change():
        print()
        hostname = input('Enter the name of the host you would like ->: ')
        f = open('/etc/hosts', 'r')
        f2 = open('/etc/hostname', 'r')
        filedata = f.read()
        filedata2 = f2.read()
        f.close()
        f2.close()

        newdata = filedata.replace('raspberrypi', hostname)
        newdata2 = filedata2.replace('raspberrypi', hostname)
        f = open('/etc/hosts', 'w')
        f2 = open('/etc/hostname', 'w')
        f.write(newdata)
        f2.write(newdata2)
        print('/etc/hosts is successfully changed')
        print('')
        print('/etc/hostname is successfully changed')
        f.close()
        f2.close()
