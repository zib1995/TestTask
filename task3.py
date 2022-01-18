
# Решение задания 3

from tqdm import tqdm

# Несколько подходящих адресов:
# https://api.github.com
# http://google.ru

# Количество запросов
total = 1000

# Вариант с синхронными запросами. Отправка следующего запроса не начнется пока не получен ответ от сервера
def sync_requests():
    import requests

    adr = input('Введите адресс интернет ресурса >')
    print('Количество отправленных запросов:')
    for _ in tqdm(range(total)):
        requests.get(adr)
    print('Все запросы выполнены')
#

# Вариант с асинхронными запросами. Запросы отправляются без ожидания ответа от сервера
def async_requests():
    import grequests

    adr = input('Введите адресс интернет ресурса >')
    answers = []
    for _ in range(total):
        answers.append(grequests.get(adr))

    print('Количество отправленных запросов:')
    for _ in tqdm(grequests.imap(answers), total = total):
        pass
    print('Все ответы получены')
#

if __name__ == '__main__':
    print('Программа отправит ' + str(total) + ' get запросов по адерсу который вы укажите.')
    print('Стоит понимать, что после такого количества запросов сервер может перестать воспринимать вас всерьез')
    async_requests()
#
