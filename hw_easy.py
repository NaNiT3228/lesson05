import os
import shutil


def dir_create(name):
    try:
        os.makedirs(name)
        print('Папка', name, 'успешно создана')
    except FileExistsError:
        print('{} - уже существует'.format(name))


def dir_delete(name):
    try:
        os.removedirs(name)
        print('Папка', name, 'успешно удалена')
    except FileNotFoundError:
        print('{} - папки не существует'.format(name))


def dir_files():
    print(os.listdir())


def dir_dir():
    buffer = os.listdir()
    for i, file in enumerate(buffer, start=1):
        if os.path.isdir(file):
            print('{}. {}'.format(i, file))


def copy_file():
    name_file = os.path.realpath(__file__)
    new_file = name_file + '.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        print(new_file + ' - создан')
    else:
        print('Копия файла уже создана')


if __name__ == '__main__':

    choose = int(input('Введите номер задания(1/2/3): '))
    # Задача-1:
    # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
    # из которой запущен данный скрипт.
    # И второй скрипт, удаляющий эти папки.
    if choose == 1:
        choose_1 = int(input('Выберите действие:\n'
                             'Создать папки в текущей дирректории - 1\n'
                             'Удалить папки в текущей дирректории - 2\n'
                             'Ваш выбор: '))
        if choose_1 == 1:
            for i in range(1, 10):
                i = str(i)
                dir_create('dir_' + i)
        elif choose_1 == 2:
            for i in range(1, 10):
                i = str(i)
                dir_delete('dir_' + i)
        else:
            print('Вы ввели что-то не то')

    elif choose == 2:
        # Задача-2:
        # Напишите скрипт, отображающий папки текущей директории.
        choose_2 = int(input('Выберите действие:\n'
                             'Отобразить все файл текущей дирректории - 1\n'
                             'Отобразить только папки текущей дирректории - 2\n'
                             'Ваш выбор: '))
        buffer = os.listdir()
        if choose_2 == 1:
            dir_files()
        elif choose_2 == 2:
            dir_dir()
        else:
            pass

    elif choose == 3:
        # Задача-3:
        # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
        choose_3 = int(input('Копировать текущий файл?\n'
                             'Да - 1\n'
                             'Нет -2\n'
                             'Ваш выбор: '))
        if choose_3 == 1:
            copy_file()
        else:
            pass
    else:
        print('Вы ввели что-то не то')
