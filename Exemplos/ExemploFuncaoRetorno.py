def somar(n1, n2):
    resultado = n1 + n2
    return resultado

def subtrair(n1, n2):
    resultado = n1 - n2
    return resultado

def multiplicar(n1, n2):
    resultado = n1 * n2
    return resultado

def dividir(n1, n2):
    resultado = n1 / n2
    return resultado

numero1 = 4
numero2 = 2

resultadoDaSoma = somar(numero1, numero2)
resultadoDaSubt = subtrair(numero1, numero2)
resultadoDaMult = multiplicar(numero1, numero2)
resultadoDaDivi = dividir(numero1, numero2)

print(f"Para os números {numero1} e {numero2}")
print("o resultado para as 4 operações de matemática são:")
print(f"Soma = {resultadoDaSoma}")
print(f"Subtração = {resultadoDaSubt}")
print(f"Multiplicação = {resultadoDaMult}")
print(f"Divisão = {resultadoDaDivi}")