while True:
    x = int(input('Deseja ver qual tabuada: '))
    if x <= 0:
        break
    for c in range (1, 11):
        print(f'{x} x {c} = {x*c}')