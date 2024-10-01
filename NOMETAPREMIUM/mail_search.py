import requests
from pystyle import Colors, Write

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

if __name__ == "__main__":
    main()