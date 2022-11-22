try:
    manager1 = int(input('summafirstmanager->'))
    manager2 = int(input('summasecondmanager->'))
    manager3 = int(input('summathirdmanager->'))
    print('#>-----<MENU>------<#')
    print('|   manager1 |')
    print('|     manager2    |')
    print('|    manager3    |')
    print('#>------------------<#')
    action = input('->')
    if action == 'manager1':
        if manager1 <= 500:
            summa1 = (200+(200 * 3 / 100))
        elif 500 < manager1 > 1000:
            summa1 = (200+(200 * 5 / 100))
        elif manager1 > 1000:
            summa1 = (200+(200 * 8 / 100))
        print(summa1)
    elif action == 'manager2':
        if manager2 <= 500:
            summa2 = (200+(200 * 3 / 100))
        elif 500 < manager2 > 1000:
            summa2 = (200+(200 * 5 / 100))
        elif manager2 > 1000:
            summa2 = (200+(200 * 8 / 100))
        print(summa2)
    elif action == 'manager1':
        if manager1 <= 500:
            summa3 = (200+(200 * 3 / 100))
        elif 500 < manager1 > 1000:
            summa3 = (200+(200 * 5 / 100))
        elif manager1 > 1000:
            summa3 = (200+(200 * 8 / 100))
        print(summa3)
    elif action == 'max3':
        if summa2 < summa1 > summa3
        total1=(summa1 + 200)
        elif summa1 < summa2 > summa3
        total2 = (summa2 + 200)
        elif summa2 < summa3 > summa1
        total1 = (summa3 + 200)
    else:
        print(f'Comand not found')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
output()