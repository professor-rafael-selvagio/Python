from click import clear
clear()


d = {'p1': 'br', 'p2': 'jp', 'p3': 'it'}

#print(d['p1'])

for c in d.keys():
    print(f'{c} -> {d[c]}')

print()

for c, v in d.items():
    print(f'{c} -> {v}')

