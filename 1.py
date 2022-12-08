try:
    start =  int(input('start->'))
    end =  int(input('end->'))
    sum = 0
    for item in range(start,end + 1):
        sum += item
    print(sum)
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
