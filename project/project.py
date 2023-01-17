import sys
import os
import sqlite3
from datetime import datetime
import urllib.request
from selenium import webdriver
from time import sleep
from threading import Thread

PATH_TO_DIR = "test/"
PATH_TO_DB = "db/"
URLS = []
DATA = []


def set_paths():
    global PATH_TO_DIR, PATH_TO_DB
    try:
        PATH_TO_DIR = sys.argv[1]
    except IndexError:
        do_nothing = None
    try:
        PATH_TO_DB = sys.argv[2]
    except IndexError:
        do_nothing = None
    print(f"[{datetime.now()}]: Заданы пути к данным")


def get_urls():
    global URLS
    try:
        for root, dirs, files in os.walk(PATH_TO_DIR):
            for name in files:
                URLS += open(os.path.join(root, name)).readlines()
                print(f"[{datetime.now()}]: Прочитан файл {name}")
        print(f"[{datetime.now()}]: Прочитана директория с файлами")
    except Exception:
        print(f"[{datetime.now()}]: Ошибка чтения директории с файлами")


def get_screenshot(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        sleep(1)
        base64 = driver.get_screenshot_as_base64()
        driver.quit()
        return base64
    except Exception:
        print(f"[{datetime.now()}]: Ошибка получения скриншота")


def get_data_for_table(url):
    global DATA
    url = url.replace("\n", "")
    try:
        status = urllib.request.urlopen(url).getcode()
    except urllib.error.HTTPError:
        status = 403

    screenshot = 0
    if status == 200:
        screenshot = get_screenshot(url)

    DATA.append([url, status, screenshot])


def update_database():
    global PATH_TO_DIR, URLS
    try:
        db_name = os.path.join(PATH_TO_DB, "temp_SQLite.db")
        db = sqlite3.connect(db_name)
        cur = db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS urls (id integer primary key AUTOINCREMENT NOT NULL, "
                    "url_name varchar(300), "
                    "status integer, "
                    "screenshot varbinary)")

        print(f"[{datetime.now()}]: Подключена база данных")
        threads = []
        for url in URLS:
            thread = Thread(target=get_data_for_table, args=(url,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        for data in DATA:
            cur.execute(f"INSERT INTO urls (url_name, status, screenshot) VALUES ('{data[0]}', {data[1]}, '{data[2]}')")

        print(f"[{datetime.now()}]: В базу данных добавлены ссылки")
        db.commit()
        print(f"[{datetime.now()}]: Работа с данными завершена")

    except Exception:
        print(f"[{datetime.now()}]: Ошибка подключения базы данных")


def delete_db():
    try:
        os.remove(PATH_TO_DB + "temp_SQLite.db")
    except FileNotFoundError:
        do_nothing = None


if __name__ == "__main__":
    delete_db()
    set_paths()
    get_urls()
    update_database()
