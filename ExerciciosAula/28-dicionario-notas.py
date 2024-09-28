from click import clear
clear()


import pprint

notas = {
    'ana': {'mat': 10, 'geo': 6, 'bio': 5},
    'juca': {'mat': 5, 'geo': 4, 'bio': 6}
}

for aluno, materias in notas.items():
    print(f"Aluno: {aluno.capitalize()}")
    for materia, nota in materias.items():
        print(f"  {materia.capitalize()}: {nota}")
    print()  # Linha em branco para separar os alunos





