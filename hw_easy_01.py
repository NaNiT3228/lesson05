# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os

choose = int(input('Выберите действие:\n'
               'Создать папки в текущей дирректории - 1\n'
               'Удалить папки в текущей дирректории - 2\n'
               'Ваш выбор: '))
if choose == 1:
    for i in range(1, 10):
        i = str(i)
        try:
            os.makedirs('dir_' + i)
        except FileExistsError:
            print('Такой файл', 'dir_' + i, 'уже существует')
elif choose == 2:
    for i in range(1, 10):
        i = str(i)
        try:
            os.removedirs('dir_' + i)
        except FileNotFoundError:
            print('Такого файла', 'dir_' + i, 'не сущестует')
else:
    print('Вы ввели что-то не то')