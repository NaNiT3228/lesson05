# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

choose = int(input('Выберите действие:\n'
               'Отобразить все файл текущей дирректории - 1\n'
               'Отобразить только папки текущей дирректории - 2\n'
               'Ваш выбор: '))

buffer = os.listdir()

if choose == 1:
    print(os.listdir())
elif choose == 2:
    for i, file in enumerate(buffer, start = 1):
        if os.path.isdir(file):
            print('{}. {}'.format(i, file))
else:
    pass