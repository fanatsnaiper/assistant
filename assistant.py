import os
import configparser

def main(): 
    try:
        config = configparser.ConfigParser()  # опостылевший конфигпарсер.конфигпарсер.конфигпарсер.конфигпарсер
        config.read('config.ini')
        program_dir = os.path.dirname(os.path.abspath(__file__))
        design_dir = f'{program_dir}/{config["Default_Dir"]["design"]}' #адрес папки design
        if os.path.exists(design_dir):
            import main_menu
            main_menu.main()
    except Exception as e:  # см Заметки пункт 3.1
        print(e)    # тут должен вызываться .bat файл для проверки целотсности окружения приложения и вывода осведомительной информации пользователю

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()