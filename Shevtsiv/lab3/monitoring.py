#!/usr/bin/env python3
import requests
import json
import logging
from requests.exceptions import HTTPError
import time

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    try:
        r = requests.get(url)
    except Exception as err:
        logging.error("Виникла помилка: : %s", err)
        print("Виникла помилка: ", err)
    else:
        print("Сервер працює!")
        data = json.loads(r.content)
        logging.info("Сервер доступний. Час на сервері: %s", data['date'])
        logging.info("Запитувана сторінка: : %s", data['current_page'])
        logging.info("Відповідь сервера місти наступні поля:")
        for key in data.keys():
            logging.info("Ключ: %s, Значення: %s", key, data[key])


    while True:
        time.sleep(60)
        main(url)


if __name__ == '__main__':
    main("http://localhost:8000/health")
