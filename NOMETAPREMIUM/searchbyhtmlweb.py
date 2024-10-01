import requests
from pystyle import Write, Colors

current_theme = Colors.white_to_green


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