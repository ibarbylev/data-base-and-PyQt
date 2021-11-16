"""Получение кода завершения подпроцесса"""

import platform
from subprocess import Popen

PROGRAM = 'regedit.exe' if platform.system() == 'Windows' else 'libreoffice'
PROCESS = Popen(PROGRAM)
