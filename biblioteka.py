import os
import shutil
import sys
import platform

def decor_menu(f_menu):
    def inner(*args, **kwargs):
        print()
        print('#' * 51)
        print('*' * 11, 'Не только файловый менеджер', '*' * 11)
        print('#' * 51)
        result = f_menu(*args, **kwargs)
        return result

    return inner

def add_separ(f):
    def inner():
        print('$'*51)
        result = f()
        return result
    return inner

@decor_menu
def show_help():
    print(' 1 - Сделать папку?')
    print(' 2 - Покоцать (файл/папку)?')
    print(' 3 - Копировать (файл/папку)?')
    print(' 4 - Просмотр текущей папки?')
    print(' 5 - Посмотреть только папки?')
    print(' 6 - Посмотреть только файлы?')
    print(' 7 - Инфо по операционной системе')
    print(' 8 - Кто сделал это ?')
    print(' 9 - Поиграем ?')
    print(' 10 - Скоко денег у мене ?')
    print(' 11 - Пойдем в другую папку ?')
    print(' 12 - Сохраним содержимое папки в файл?')
    print(' 0 - Хватит, пошли... ???')
    print('######################@@@###########################')

@add_separ
def create_dir():
    print("")
    answer = input('Какую папку сделать -> ')
    temp_dir = os.path.join(os.getcwd(), answer)
    try:
        if os.path.exists(temp_dir):
            print("Папка уже есть. Укажите другое имя")
        else:
            os.mkdir(temp_dir)
            print("Ура, папку сделали")
            print("")
    except:
        print("Такие символы использовать в имени папки нельзя")

@add_separ
def del_file_or_dir():
    print("")
    answer = input('Введите имя файла или папки для удаления -> ')
    temp_name = os.path.join(os.getcwd(), answer)
    try:
        if os.path.exists(temp_name):  
            if os.path.isfile(temp_name):   
                os.remove(temp_name)
                print("Файл удалён")
            elif os.path.isdir(temp_name):  
                shutil.rmtree(temp_name)
                print("Папка  удалена")
        else:
            print("Данный файл/папка не найдена в текущей папки")
    except:
        print(" Ошибка удаления файла/папки -  доступа нет")

@add_separ
def copy_file_or_dir():
    print("")
    src_answer = input('Имя файла/папки для копирования -> ')
    dest_answer = input('Введите новое имя файла/папки -> ')
    if src_answer == dest_answer:
        print("Имя файла/папки уже есть. Повторите ввод.")
    else:
        src_answer = os.path.join(os.getcwd(), src_answer)
        dest_answer = os.path.join(os.getcwd(), dest_answer)
        if not os.path.exists(src_answer):
            print("Файл/папка не найден")
        else:
            try:
                if os.path.isfile(src_answer):          # TRY
                    shutil.copy2(src_answer, dest_answer)
                    print("Файл скопирован")
                elif os.path.isdir(src_answer):         # Директория
                    shutil.copytree(src_answer, dest_answer)
                    print("Папка скопирована")
            except IOError as e:
                print(f'ОШИБКА. {e.strerror}')

@add_separ
def find_all_in_current_dir():
    folders = []
    print("Список папок и файлов в текущей папке со всеми вложенными:")
    for item in os.walk(os.getcwd()):
        folders.append(item)

    for address, dirs, files in folders:
        for dir in dirs:
            for file in files:
                print(f"Директория: {os.path.join(address, dir)}, Файл: {file}")

@add_separ
def get_files_in_current_dir():
    print("Список файлов здесь")
    print("\n".join(list(filter(lambda x: os.path.isfile(x), os.listdir(".")))))
    print()

@add_separ
def get_dir_in_current_dir():
    print("Список папок в здесь:")
    print("\n".join(list(filter(lambda x: os.path.isdir(x), os.listdir(".")))))
    print()
@add_separ
def get_system_info():
    print()
    print("Посмотрим систему:")
    ops, name, oper_ver, build, proc, proc_fam = platform.uname()
    print(f"ОС: {ops}")
    print(f"Архитектура: {platform.architecture()}")
    print(f"На чем: {sys.platform}")
    print(f"Версия ОС: {oper_ver}")
    print(f"Релиз ОС: {build}")
    print(f"Юзер: {name}")
    print()
    print(f"Проц: {proc}")
    print(f"Модель проца: {proc_fam}")
    print()
    print(f"Версия Python: {' от '.join(platform.python_build())}")
    print(f"Версия компилятора Python: {platform.python_compiler()}")
    print(f"Реализация Python: {platform.python_implementation()}")
    print(f"Папка  Python: {sys.prefix}")
    print()

@add_separ
def change_current_dir():
    dir = os.getcwd()
    print(f"Текущая папка: {dir}")
    answer = input('Куда пойдем?: -> ')
    try:                   # TRY
        os.chdir(answer)
        print(f"Мы здесь: {os.getcwd()}")
    except BaseException as e:
        print(f'ОШИБКА: {e.strerror}')
        os.chdir(dir)
        print(f"Мы на месте: {os.getcwd()}")
@add_separ
def save_current_dir():
    content = os.listdir()
    files = filter(lambda x: os.path.isfile(x), content)
    dirs = filter(lambda x: os.path.isdir(x), content)
    with open('listdir.txt', 'w') as f:
        f.write('files: ')
        for file in files:
            f.write(f'{file}, ')
        f.write('\n')
        f.write('dirs: ')
        for dir in dirs:
            f.write(f'{dir}, ')

