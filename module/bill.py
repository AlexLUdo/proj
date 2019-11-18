# my bill
def moj_schet():
    import os
    import json

    FILE_NAME = 'account.json'

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            account = json.load(f)
    else:
        account = {'acc_balance': 0, 'shop_list': []}

    # main menu
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню :) ')
        if choice == '1':
            account['acc_balance'] += acc_repl()
            print('Остаток счета {0:8.2f} $'.format(account['acc_balance']))
        elif choice == '2':
            account = shop_action(account)
        elif choice == '3':
            shop_history(account['shop_list'])
        elif choice == '4':
            with open('account.json', 'w') as f:
                json.dump(account, f)
            print('Thanks за покупки! Ждем вас снова!')
            break
        else:
            print('Неверный пункт меню')


def acc_repl():  # add money
    return(float(input('Введите сумму пополнения счета:')))

def shop_history(shop_list):  # buy history
    if len(shop_list) == 0:
        print('Покупок еще нет!')
    else:
        print('История покупок:')
        for item in shop_list:
            print(item[0], item[1], '$')
    return(shop_list)


def shop_action(acc):  # make buy
    suma  = input('Введите сумму покупки:')
    try:
        suma = int(suma)
    except ValueError:
        print("Сумма покупки - это число")
        return acc
    if suma > acc['acc_balance']:
        print('Денег на счете не хватает!')
    else:
        name = input('Введите название покупки:')
        acc['acc_balance'] -= suma
        acc['shop_list'].append([name, suma])
    return acc


    FILE_NAME = 'account.json'

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            account = json.load(f)
    else:
        account = {'acc_balance': 0, 'shop_list': []}

    # цикл основного меню
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню :) ')
        if choice == '1':
            account['acc_balance'] += acc_repl()
            print('Остаток счета {0:8.2f} $'.format(account['acc_balance']))
        elif choice == '2':
            account = shop_action(account)
        elif choice == '3':
            shop_history(account['shop_list'])
        elif choice == '4':
            with open('account.json', 'w') as f:
                json.dump(account, f)
            print('Спасибо за покупки! Ждем вас снова!')
            break
        else:
            print('Неверный пункт меню')


def acc_repl():  # add money
    return(float(input('Введите сумму пополнения:')))

def shop_history(shop_list):  # print history of purchases
    if len(shop_list) == 0:
        print('Покупок еще нет :(')
    else:
        print('История покупок:')
        for item in shop_list:
            print(item[0], item[1], '$.')
    return(shop_list)


def shop_action(acc):  # make purchase
    suma = float(input('Введите сумму покупки $:'))
    if suma > acc['acc_balance']:
        print('$ на счете не хватает! :(')
    else:
        name = input('Введите название покупки:')
        acc['acc_balance'] -= suma
        acc['shop_list'].append([name, suma])
    return acc
