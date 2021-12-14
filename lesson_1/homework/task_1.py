"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping
будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел
должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять
их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес
сетевого узла должен создаваться с помощью функции ip_address().
"""

import os
import subprocess
from ipaddress import ip_address

hosts_list = ['192.168.8.1', '8.8.8.8', 'yandex.ru']  # список проверяемых хостов
result = {'Доступные узлы': "", "Недоступные узлы": ""}  # словарь с результатами

DNULL = open(os.devnull, 'w')  # заглушка, чтобы поток не выводился на экран
# https://stackoverflow.com/questions/52435965/difference-between-os-devnull-and-subprocess-pipe


def check_is_ipaddress(value):
    """
    Проверка является ли введённое значение IP адресом
    :param value: присланные значения
    :return ipv4: полученный ip адрес из переданного значения
        Exception ошибка при невозможности получения ip адреса из значения
    """
    try:
        ipv4 = ip_address(value)
    except ValueError:
        raise Exception('Некорректный ip адрес')
    return ipv4


def host_ping(hosts_list, get_list=False):
    """
    Проверка доступности хостов
    :param hosts_list: список хостов
    :param get_list: признак нужно ли отдать результат в виде словаря (для задания #3)
    :return словарь результатов проверки, если требуется
    """
    print("Начинаю проверку доступности узлов...")
    for host in hosts_list:  # проверяем, является ли значение ip-адресом
        try:
            ipv4 = check_is_ipaddress(host)
        except Exception as e:
            print({host} - {e}, 'воспринимаю как доменное имя')
            ipv4 = host
        response = subprocess.Popen(["ping", str(ipv4)], stdout=DNULL)
        if response == 0:
            result["Доступные узлы"] += f"{str(ipv4)}\n"
            res_string = f"{str(ipv4)} - Узел доступен"
        else:
            result["Недоступные узлы"] += f"{ipv4}\n"
            res_string = f"{str(ipv4)} - Узел недоступен"
        if not get_list:  # если результаты не надо добавлять в словарь, значит отображаем
            print(res_string)
    if get_list:        # если требуется вернуть словарь (для задачи №3), то возвращаем
        return result


if __name__ == '__main__':
    host_ping(hosts_list)
    print(result)
