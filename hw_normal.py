import os
import hw_easy as nanitqq


def change_dir(path):
    try:
        os.chdir(path)
        return 'Успешно перешли в папку: {}'.format(path)
    except FileNotFoundError:
        return '{} - папки не существует'.format(path)

choose = ' '

while choose != 5:
    choose = int(input('Выберите действие:\n'
                       '1. Перейти в папку\n'
                       '2. Просмотреть содержимое текущей папки\n'
                       '3. Удалить папку\n'
                       '4. Создать папку\n'
                       '5. Выйти из программы\n'
                       'Ваш выбор: '))
    if choose == 1:
        path_name = input('Введите название папки, в которую хотите перейти: ')
        print(change_dir(path_name))
    elif choose == 2:
        nanitqq.dir_files()
    elif choose == 3:
        name = input('Введите имя папки которую вы хотите удалить: ')
        nanitqq.dir_delete(name)
    elif choose == 4:
        name = input('Введите название папки котрую хотите добавить: ')
        nanitqq.dir_create(name)
    else:
        print('Был совершен выход из программы')