from click import clear
clear()

def par(n):
    if n % 2 == 0:
        return True

ret = par(2)
if not ret:
    print('Impar')
else:
    print('Par')