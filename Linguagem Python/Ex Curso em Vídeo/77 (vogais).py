x = ('Maria', 'Bernadete', 'Paulo', 'Carlos')
for c in x:
    print(f'\nNa palavra {c.upper()} temos ', end=' ')
    for x in c:
        if x.lower() in 'aeiou':print(x, end=' ')
