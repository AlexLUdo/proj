# в файл менеджере все функции "грязные", одолжил несколько функций из вашего примера, сами функции в alex_functions.py
import alex_functions

def test_author_info():
    assert alex_functions.author_info() == 'Alex Udo'

def test_separator():
    assert alex_functions.separator(10) == '**********'

def test_is_correct_choice():
    assert alex_functions.is_correct_choice('6') == True

# грязная функция, не сработает в других местах
def test_filenames():
    assert alex_functions.filenames() == ['.gitignore', 'alex_functions.py', 'biblioteka.py', 'filemanager.py', 'file_manager.py', 'functions.py', 'main.py', 'osnovnoe.py']
