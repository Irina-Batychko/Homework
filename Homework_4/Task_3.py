""" Задача №3
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""


def atm_machine():
    while True:
        global summ
        global bill
        action = input("Выберете действие:\n Пополнить\n Снять\n Выйти\n")
        if summ > 5_000_000:
            print("Удержан налог на богатство в размере 10% от суммы на счету: ", int(summ * 0.1))
            bill.append(-int(summ * 0.1))
            summ = int(summ * 0.9)
            print("Остаток на счете:", summ)

        match (action.lower()):
            case "пополнить":
                deposit_money()
            case "снять":
                withdraw_money()
            case "выйти":
                break
            case _:
                print("Пожалуйста, повторите попытку. Вы ввели некорректные данные.")


def deposit_money():
    global summ
    global i
    global j
    global bill
    put = int(input("Введите сумму пополнения, внесено будет кратно 50: "))
    put = (put // 50) * 50
    if i % 3 == 0:
        print("Процент за пополнение: 3% от суммы пополнения")
        commission_percent = 0.03
    else:
        commission_percent = 0
    commission = int(commission_percent * put)
    summ = int(summ + put - commission)
    bill.append(put - commission)
    i += 1
    j = 1
    print("Комиссия: ", commission, "Внесено: ", put - commission)
    print("Остаток на счете: ", summ)
    return


def withdraw_money():
    global summ
    global j
    global i
    global bill
    min_commission = 30
    max_commission = 600
    take_off = int(input("Введите сумму снятия, кратно 50: "))
    take_off = (take_off // 50) * 50
    if take_off > summ:
        print("Сумма снятия превышает остаток на счете!")
    else:
        if j % 3 == 0:
            print("Процент за снятие: 3% от суммы снятия, но не менее 30 и не более 600 у.е.")
            commission_percent = 0.03
        else:
            print("Процент за снятие: 1,5% от суммы снятия, но не менее 30 и не более 600 у.е.")
            commission_percent = 0.015
        commission = commission_percent * take_off
        if commission < min_commission:
            commission = min_commission
        elif commission > max_commission:
            commission = max_commission
        print("Сумма на счете: ", summ, "Планируемая сумма снятия: ", take_off, "Планируемая комиссия: ", commission)
        if take_off + commission > summ:
            print("Недостаточно средств на счете для снятия с учетом комиссии!")
        else:
            summ = summ - take_off - commission
            bill.append(-(take_off - commission))
            print("Остаток на счете: ", summ)
            j += 1
            i = 1


summ = 0
i = 1
j = 1
bill = []
atm_machine()
print(bill)
