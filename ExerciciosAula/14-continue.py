from click import clear
clear()

# continue - exemplo
n = 5
print("The continue instrução:")
for i in range(1, 11):
    if i == 3:
        continue
        
    print(f'{n} x {i} = {n * i}')

print("Fora do loop.")