
def osnovnoe_menu():
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

def moj_schet():
    current_del = "\n"
    account = float("0.0")
    pay_history = []
    while True:
        osnovnoe_menu()

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            user_sum = input('Укажите сумму пополнения счета, разделитель - точка: ')
            try:
                if float(user_sum) <= 0:      # float
                    raise Exception("Введено не правильное значение")
                account += float(user_sum)
            except:
                print("Указана не правильная сумма пополнения счета")
            print(f"Текущее состояние счета: {account}")
        elif choice == '2':
            pay_sum = input('Укажите сумму покупки, разделитель - точка: ')
            try:
                if float(pay_sum) <= 0:
                    raise Exception("Введено не корректное значение")
                pay_sum = float(pay_sum)
            except:
                print("Указана не правильная сумма предполагаемой покупки")
                continue
            if account < pay_sum:
                print(f"Нет денег для покупки. На счете: {account}")
            else:
                pay_name = input('Название покупки: ')
                account -= pay_sum
                while not pay_name.isalpha():
                    pay_name = input('Название  покупки: ')
                pay_history.append(f"Товар: {pay_name}; Стоимость: {pay_sum}")
                print(f"Текущее состояние счета: {account}")
        elif choice == '3':
            if len(pay_history) == 0:
                print("Покупок нет")
            else:
                print("История покупок: ")
                print(current_del.join(pay_history))
        elif choice == '4':
            break
        else:
            print('Нет такого пункта меню')

    print('Приходите ещё!)')
