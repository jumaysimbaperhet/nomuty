import csv
import sqlite3
import pandas as pd
import time
from pystyle import Write, Colors

def format_output(file_path, nm, keys, values):
    formatted_lines = []
    for i, (key, value) in enumerate(zip(keys, values)):
        clean_value = str(value).replace(';', '\n').replace('\n', ' ')
        formatted_lines.append(f"{key}: {clean_value}")
    return f"[Файл: {file_path} | Строка: {nm}]\n" + "\n".join(formatted_lines) + "\n" + '-'*50

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
                Write.Print(f"\n🔍 Найдено в {file_path}, лист {sheet_name}:\n{formatted_output}", Colors.white_to_green)
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
                Write.Print(f"\n🔍 Найдено в {file_path}, таблица {table[0]}:\n{formatted_output}", Colors.white_to_green)
                time.sleep(0.00005)  # Интервал
                found += 1
    conn.close()
    if found == 0:
        Write.Print(f"\n❌ По запросу '{search_term}' ничего не найдено в базе данных {file_path}.", Colors.white_to_green)
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

