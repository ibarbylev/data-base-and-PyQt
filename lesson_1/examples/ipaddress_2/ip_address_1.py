"""
Python для сетевых инженеров

Модуль ipaddress упрощает создание, редактирование, манипуляцию с IP-адресами
и сетями начиная с Python 3.3. (тогда он появился)

Классы и функции в этом модуле позволяет упростить решение различных задач,
связанных с IP-адресами. Например, проверка находятся ли два хоста в одной подсети,
возможность перебрать хосты в подсети, преобразование строки в IP-адрес.
"""
import locale
import socket
import subprocess
from ipaddress import ip_address

# Функция ipaddress.ip_address()
# позволяет создавать объект IPv4Address или IPv6Address

# создание IPv4-адреса
# протокол версии ip4 используется в старых виндовсах (до хр )
# а ip6 в висте и дальше, это для настройки сети и интернета

"""
в IPv6-адресе 128 бит представляет собой целых восемь 16-битных 16-теричных блоков, 
которые разделены двоеточиями. Пример: 2dfc:0:0:0:0217:cbff:fe8c:0. 
Если же говорить про адрес IPv4, то традиционной формой его записи является запись 
в виде 4-х десятичных чисел от 0 до 255, которые разделены точками, 
а через дробь обозначается длина маски подсети. Пример: 192.168.0.0/16
"""

# Finding Your Public IP Address
proc = subprocess.Popen('curl -sS ifconfig.me/ip'.split(), stdout=subprocess.PIPE)
my_public_ip = proc.stdout.read().decode(locale.getpreferredencoding())
print(my_public_ip)

# Finding Your Local IP Address
my_local_ip = socket.gethostbyname(socket.gethostname())
print(my_local_ip)

ip_for_testing = '198.186.1.0'
IPV4 = ip_address(ip_for_testing)
print(type(IPV4))
print(IPV4)

# набор специальных методов и атрибутов
# 127.0.0.1 — это адрес интернет-протокола loopback (IP),
# также называемый «localhost». Адрес используется для установления
# соединения с тем же компьютером, который используется конечным пользователем.
# is_loopback - возвращает True, если находит loopback-адрес
# https://ru.wikipedia.org/wiki/Loopback
print(IPV4.is_loopback)

# is_multicast - возвращает True, если находит multicast-адрес
# групповой адрес адрес, определяющий группу станций локальной сети,
# одновременно получающих сообщение
# https://ru.wikipedia.org/wiki/Мультивещание
print(IPV4.is_multicast)

# is_reserved - возвращает True, если находит IETF-зарезервированный адрес
# Инжене́рный сове́т Интерне́та (англ. Internet Engineering Task Force, IETF) —
# открытое международное сообщество проектировщиков, учёных, сетевых операторов и провайдеров,
# созданное IAB в 1986 году и занимающееся развитием протоколов и архитектуры Интернета.
# Зарезервированные адреса -
# это диапазон адресов ,зарезервированный и закрепленный для использования в частной сети.
# Зарезервированные адреса не могут использоваться для доступа к сети интернет.
print(IPV4.is_reserved)

# is_private - возвращает True, если адрес выделен для частных сетей
# Частный IP-адрес[1][2] (англ. private IP address), также называемый внутренним,
# внутрисетевым, локальным или «серым» — IP-адрес, принадлежащий к специальному диапазону,
# не используемому в сети Интернет. Такие адреса предназначены для применения в локальных сетях,
# распределение таких адресов никем не контролируется. В связи с дефицитом свободных IP-адресов,
# провайдеры всё чаще раздают своим абонентам именно внутрисетевые адреса,
# а не внешние, при этом один внешний айпи выдаётся нескольким клиентам.
# https://ru.wikipedia.org/wiki/%D0%A7%D0%B0%D1%81%D1%82%D0%BD%D1%8B%D0%B9_IP-%D0%B0%D0%B4%D1%80%D0%B5%D1%81
print('is_private: ', IPV4.is_private)

# операции с объектами-адресами
IP1 = ip_address('192.168.1.0')
IP2 = ip_address('192.168.1.255')

# сравнение ip-адресов
if IP2 > IP1:
    print('IP2 > IP1: ', True)

# конвертация ip-адреса в строку
print(str(IP1))

# конвертация ip-адреса в целое число
# 192.168.1.0 --> 3232235776
print(int(IP1))

# альтернативный способ вычисления ip-адреса как целого числа
address_bytes = [int(x) for x in '192.168.1.0'.split('.')]
ip_int = (
    address_bytes[0] * (256 ** 3) +
    address_bytes[1] * (256 ** 2) +
    address_bytes[2] * (256 ** 1) +
    address_bytes[3] * (256 ** 0)
)
print(ip_int)

# изменение идентификатора узла в сети
# 192.168.1.0 + 5 = 192.168.1.5
print(IP1 + 5)

# 192.168.1.0 - 5 = 192.168.0.251
print(IP1 - 5)
