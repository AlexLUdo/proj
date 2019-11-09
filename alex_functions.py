import os
def author_info():
    return 'Alex Udo'

def separator(count=33):
    return '*' * count
COPY_FILE_FOLDER = 'Копировать (файл/папку)'
SHOW_FILES = 'Посмотреть только файлы'
AUTHOR = 'Создатель программы'
VICTORY = 'Играть в викторину'
BILL = 'Мой банковский счет'
EXIT = 'Выход'

# Набор пунктов меню
menu_items = (
    COPY_FILE_FOLDER,
    SHOW_FILES,
    AUTHOR,
    VICTORY,
    BILL,
    EXIT
)


def is_correct_choice(choice):
    return choice.isdigit() and int(choice) > 0 and int(choice) <= len(menu_items)


def filenames():
    result = []
    for item in os.listdir():
        if os.path.isfile(item):
            result.append(item)
    return result


print(filenames())

