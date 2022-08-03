"""
In this example run multiple subprocesses simultaneously.
And get ip address from method Popen.args
"""

import locale
import platform
from subprocess import Popen, PIPE

ENCODING = locale.getpreferredencoding()
result = {'Reachable': "", "Unreachable": ""}


def host_ping(hosts_list, get_list=False) -> result:
    """
    Host availability check
    """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = [['ping', param, '1', '-w', '1', ip] for ip in hosts_list]
    processes = [Popen(args, stdout=PIPE, stderr=PIPE) for args in args]

    for process in processes:
        code = process.wait()
        new_ip = process.stdout.read().decode(ENCODING).split()[1]
        if code == 0:
            result['Reachable'] += new_ip
            print('Reachable', new_ip) if not get_list else None
        else:
            result['Unreachable'] += new_ip
            print('Unreachable', new_ip) if not get_list else None

    if get_list:
        return result


if __name__ == '__main__':
    hosts_list = ['192.168.8.1', '8.8.8.8', 'ya.ru', 'google.com',
                  '0.0.0.1', '0.0.0.2', '0.0.0.3', '0.0.0.4', '0.0.0.5',
                  '0.0.0.6', '0.0.0.7', '0.0.0.8', '0.0.0.9', '0.0.1.0',
                  '171.15.131.14', '127.0.0.25']
    host_ping(hosts_list)
