import serial #for Serial communication

class Board_connect():
    def main(self,connection_params):   #   эта функция открывает порт для работы
        self.board = serial.Serial(connection_params[0],connection_params[1])   # открывает порт с заданными параметрами
            
    def send(self,command): #   эта функция обрабатывает и передает команды
        if command != 'stop':
            self.board.write(f"{command}".encode())
        #доработать код. в этом месте обрабатывается команда на закрытие работы с ардуино, оно же по сути закрывает многопоточность и даёт возможность спокойно использовать sys.exit() 
        elif command == 'stop':
            print(3)
            return False    # именно этот return закрывает многопоточность и позволяет основному приложению спокойно закрываться