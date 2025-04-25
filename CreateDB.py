
import sqlite3
import pandas as pd

def create_db(path_to_xlsx):
    # Чтение данных из Excel
    xls = pd.ExcelFile(path_to_xlsx)
    # Чтение данных из каждого листа, начиная со второй строки (первая строка — заголовки)
    df_expenses = pd.read_excel(xls, sheet_name="Расходы", header=1)
    df_income = pd.read_excel(xls, sheet_name="Доходы", header=1)
    df_trans = pd.read_excel(xls, sheet_name="Переводы", header=1)
    create_table_and_insert_data("Expenses", df_expenses)
    print()
    create_table_and_insert_data("Income", df_income)

def create_table_and_insert_data(table_name, df):
    # Подключение к базе данных
    conn = sqlite3.connect("wallet.db")
    cursor = conn.cursor()

    # Создание таблицы
    columns = ", ".join([f'"{col}" TEXT' for col in df.columns])  # Все столбцы как TEXT
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {columns})")

    # Вставка данных в таблицу
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()
    print(f"1) Таблица {table_name} создана и данные записаны.")
    if table_name != "Transactions":
        delete_columns(table_name)

def delete_columns(table_name):
    conn = sqlite3.connect("wallet.db")
    cursor = conn.cursor()
    # Создаем новую таблицу
    cursor.execute(f"""CREATE TABLE {table_name}_new AS
    SELECT 
        "Дата и время",
        "Категория",
        "Счет",
        "Сумма в валюте счета",
        "Теги",
        "Комментарий"
    FROM {table_name};""")
    print("2) Переписываем данные")
    # Удаляем старую таблицу
    cursor.execute(f"DROP TABLE {table_name};")
    print("3) Удаляем таблицу")
    # Переименовываем таблицу
    cursor.execute(f"ALTER TABLE {table_name}_new RENAME TO {table_name};")
    print(f"4) Переименовываем таблицу в {table_name} ")

    # Принимаем изменения 
    conn.commit()
    conn.close()
