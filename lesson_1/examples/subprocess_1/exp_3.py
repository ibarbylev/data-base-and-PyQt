"""Получение кода завершения подпроцесса"""

import platform
from subprocess import Popen

'''
Здесь мы создали переменную под названием program и назначили ей значение notepad.exe. 
После этого мы передали её классу Popen. После запуска этого кода, вы увидите, 
что он мгновенно вернет объект subprocess.Popen, а вызванное приложение будет выполняться. 
'''

# VARIANT 1
# сравните = не ждать закрытия приложения
COMMAND = 'regedit.exe' if platform.system() == 'Windows' else 'libreoffice'
PROCESS = Popen(COMMAND)

print(PROCESS)

# VARIANT 2
# и это = ждать закрытия приллжения
PROCESS = Popen(COMMAND)
CODE = PROCESS.wait()

print(PROCESS)
print(CODE)
