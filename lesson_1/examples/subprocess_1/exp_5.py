"""Запуск скрипта-дочернего процесса"""

import platform
from subprocess import Popen, PIPE

PROGRAM = 'regedit.exe' if platform.system().lower() == 'windows' else 'libreoffice'
process = Popen(
    PROGRAM,
    shell=True,
    stdout=PIPE, stderr=PIPE
)

# получить tuple('stdout', 'stderr')
result = process.communicate()
print(process.returncode)
if process.returncode == 0:
    print(result)
print('result:', result[0])
