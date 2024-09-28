from click import clear
clear()

produtos = [
    {"nome": "Produto A", "estoque": 11, "valor_unitario": 20.0},  # Valor unitário em reais
    {"nome": "Produto B", "estoque": 5, "valor_unitario": 15.0},
    {"nome": "Produto C", "estoque": 13, "valor_unitario": 30.0},
]

for produto in produtos:
    if produto["estoque"] > 10:
        continue  # Ignora produtos fora de estoque
    
    # Cálculo do valor total do estoque
    valor_total = produto["estoque"] * produto["valor_unitario"]
    print(f"{produto['nome']} - estoque {produto['estoque']} - valor unitario {produto['valor_unitario']} - valor total de R$ {valor_total:.2f}")
