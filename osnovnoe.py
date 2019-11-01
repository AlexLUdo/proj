import biblioteka
import module.bill as igra_schet
import module.victory as igra_viktorina

while True:
    biblioteka.show_help()
    otvet = input('Выберите пункт меню -> ')
    if otvet == '1':
        biblioteka.create_dir()
    elif otvet == '2':
        biblioteka.del_file_or_dir()
    elif otvet == '3':
        biblioteka.copy_file_or_dir()
    elif otvet == '4':
        biblioteka.find_all_in_current_dir()
    elif otvet == '5':
        biblioteka.get_dir_in_current_dir()
    elif otvet == '6':
        biblioteka.get_files_in_current_dir()
    elif otvet == '7':
        biblioteka.get_system_info()
    elif otvet == '8': 
        print(f"Автор Alex Udo")
        print(f"30.10.2019")
        print()
    elif otvet == '9':  
        answer = input('Скоко-скоко хотите вопросов в викторине?: -> ')
        if answer.isdigit():
            count_questions = int(answer)
            if (count_questions >= 10) | (count_questions < 2):
                print("В викторине 5 вопросов")
                igra_viktorina.victory_run()
            else:
                igra_viktorina.victory_run(count_questions)
    elif otvet == '10':  
        igra_schet.moj_schet()
    elif otvet == '11':  
        biblioteka.change_current_dir()
    elif otvet == '0':  
        print('Все, пока!')
        break
    else:
        print("Не правильно. Повторите ввод.")
