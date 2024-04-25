import sys
import glob
import serial

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):  # поиск портов для устройств на виндоус
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'): # поиск портов для устройств на линукс
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'): # поиск портов для устройств на хз что это вообще
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')  # неужели и такое есть в природе

    result = []
    for port in ports:  # эта проверка тоже что-то делает (возможно, проверяет найденные порты на работоспособность/ наличие подключения)
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

if __name__ == '__main__':
    print(serial_ports())