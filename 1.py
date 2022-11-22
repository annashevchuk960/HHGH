try:
    hour = int(input('hour->'))
    minute = int(input('minute->'))
    second = int(input('second->'))
    if 0 > hour :
        raise Exception('hour can not be <  0 ')
    if 0 > minute :
        raise Exception('minute can not be <  0 ')
    if 0 > second :
        raise Exception('second can not be <  0 ')
    kievstar = float(input('kievstar->'))
    mts = float(input('mts->'))
    life= float(input('life->'))
    print('#>-----<MENU>------<#')
    print('|   kievstar |')
    print('|     mts     |')
    print('|    life    |')
    print('#>------------------<#')
    action = input('->')
    time = ((hour * 3600)+(minute * 60) + second )
    if action == 'kievstar':
        kievstar = (((kievstar * 100)/60) * time / 100  )
        print(kievstar)
    elif action == 'life':
        life = (((life * 100)/60) * time / 100 )
        print(life)
    elif action == 'mts':
        mts = (((mts * 100)/60) * time / 100 )
        print(mts)
    else:
        print(f'Comand not found')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')