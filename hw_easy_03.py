# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import shutil

choose = int(input('Копировать текущий файл?\n'
               'Да - 1\n'
               'Нет -2\n'
               'Ваш выбор: '))

if choose == 1:
    name_file = os.path.realpath(__file__)
    new_file = name_file + '.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        print(new_file + ' - создан')
    else:
        print('Копия файла уже создана')
else:
    pass