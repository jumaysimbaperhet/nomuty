import os
import platform
import asyncio
from pystyle import Colorate, Colors, Center, Write
import socket
import requests
from searchbyscorp import search
from searchbyhtmlweb import search_by_htmlweb
from mail_search import main
from searchbydb import universal_search
import time
import subprocess

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
                            Write.Print(f"\n[NM]{sub_sub_key} -> {sub_sub_value}", current_theme, interval=0.00005)
                    elif isinstance(sub_value, list) and all(isinstance(i, dict) for i in sub_value):
                        Write.Print(f"\n[NM] {sub_key} ->", current_theme, interval=0.00005)
                        for item in sub_value:
                            for item_key, item_value in item.items():
                                Write.Print(f"\n[NM] {item_key} -> {item_value}", current_theme, interval=0.00005)
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
        asyncio.run(search())
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
