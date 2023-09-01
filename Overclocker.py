class Overclocker:

    def __init__(self):
        pass

    def overclock(self):
        print('')
        overclock = int(input('Enter ClockSpeed MHZ ->: '))
        print('')
        overvoltage = int(input('Enter Over Voltage ->: '))
        f = open('/boot/config.txt', 'r')
        filedata = f.read()
        newdata = filedata.replace('#arm_freq=800',
                                   'arm_freq=' + str(overclock) + '\n' + 'over_voltage=' + str(overvoltage))
        print('')
        print('Changing File....')
        print('')
        f.close()
        f = open('config.txt', 'w')
        f.write(newdata)
        f.close()
        print('File Successfully changed....')