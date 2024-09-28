from calculadora_area import calcular_area_circulo, calcular_area_retangulo

area_circulo = calcular_area_circulo(5)
print(area_circulo) # Saída: 78.5

area_retangulo = calcular_area_retangulo(4, 6)
print(area_retangulo) # Saída: 24

''''
Note que usando o comando FROM, delimitamos apenas quais funções do  arquivo
calculadora_area serão utilizadas. A função calcular_area_triangulo não pode
ser utilizada pois não foi importada.
'''