# questions.py

import random

# Perguntas de verdadeiro ou falso
true_false_questions = [
    {
        "question": "O Power BI Desktop é gratuito para uso individual.",
        "answer": True
    },
    {
        "question": "O Power BI só permite importar dados de arquivos do Excel.",
        "answer": False
    },
    {
        "question": "As visualizações no Power BI podem ser personalizadas com diferentes cores, tamanhos e rótulos.",
        "answer": True
    },
    {
        "question": "DAX é a linguagem de programação utilizada para criar dashboards no Power BI.",
        "answer": False
    },
    {
        "question": "Podemos publicar relatórios do Power BI Desktop no Power BI Service para compartilhar online.",
        "answer": True
    },
    {
        "question": "Uma vez publicado um relatório no Power BI Service, não podemos mais realizar alterações.",
        "answer": False
    },
    {
        "question": "O Power BI permite a criação de dashboards interativos.",
        "answer": True
    },
    {
        "question": "Power Query é utilizado para criar dashboards no Power BI.",
        "answer": False
    },
    {
        "question": "Podemos utilizar o Power BI para analisar dados de redes sociais.",
        "answer": True
    },
    {
        "question": "O Power BI só é útil para empresas de grande porte.",
        "answer": False
    }
]

# Perguntas de múltipla escolha
multiple_choice_questions = [
    {
        "question": "Qual destas NÃO é uma fonte de dados válida para o Power BI?",
        "options": ["Arquivo CSV", "Banco de Dados SQL", "Página Web", "Jogo de RPG"],
        "answer": "Jogo de RPG"
    },
    {
        "question": "Qual a função DAX utilizada para calcular a soma de valores?",
        "options": ["AVERAGE", "SUM", "COUNT", "MAX"],
        "answer": "SUM"
    },
    {
        "question": "Qual a principal vantagem de se usar um dashboard no Power BI?",
        "options": ["Criar apresentações longas e detalhadas.", "Visualizar dados de forma clara e concisa.", "Armazenar grandes quantidades de dados.", "Automatizar tarefas repetitivas."],
        "answer": "Visualizar dados de forma clara e concisa."
    },
    {
        "question": "Qual o nome da ferramenta do Power BI utilizada para limpar e transformar dados?",
        "options": ["Power Pivot", "Power Query", "Power View", "Power BI Desktop"],
        "answer": "Power Query"
    },
    {
        "question": "Qual destes elementos visuais NÃO está disponível no Power BI?",
        "options": ["Gráfico de Barras", "Mapa", "Cartão", "Jogo da Velha"],
        "answer": "Jogo da Velha"
    },
    {
        "question": "Para que serve o recurso de 'Filtros' em um dashboard do Power BI?",
        "options": ["Segmentar os dados e visualizar informações específicas.", "Alterar as cores e o design do dashboard.", "Compartilhar o dashboard com outros usuários.", "Criar novas colunas e tabelas de dados."],
        "answer": "Segmentar os dados e visualizar informações específicas."
    },
    {
        "question": "Qual a finalidade da função 'Relacionamentos' no Power BI?",
        "options": ["Definir a ordem de exibição dos gráficos.", "Conectar tabelas que possuem informações em comum.", "Importar dados de diferentes fontes.", "Criar medidas calculadas."],
        "answer": "Conectar tabelas que possuem informações em comum."
    },
    {
        "question": "O que significa a sigla 'DAX'?",
        "options": ["Data Analysis Expressions", "Data Analysis Expertise", "Dashboard Analytics eXtractor", "Database Access XML"],
        "answer": "Data Analysis Expressions"
    },
    {
        "question": "No Power BI Service, o que é um 'Workspace'?",
        "options": ["Um tipo de visualização gráfica.", "Um espaço de trabalho para organizar dashboards e relatórios.", "Uma função DAX para calcular médias.", "Um tipo de arquivo de dados."],
        "answer": "Um espaço de trabalho para organizar dashboards e relatórios."
    },
    {
        "question": "Qual a importância de se utilizar o Power BI para análise de dados?",
        "options": ["Facilitar o trabalho dos desenvolvedores.", "Substituir o uso de planilhas eletrônicas.", "Transformar dados em insights valiosos para tomada de decisões.", "Criar apresentações visualmente atraentes."],
        "answer": "Transformar dados em insights valiosos para tomada de decisões."
    }
]

def get_random_question():
    """Retorna uma pergunta aleatória (pode ser verdadeiro/falso ou múltipla escolha)."""
    if random.choice([True, False]):  # Decide aleatoriamente entre as duas categorias
        return random.choice(true_false_questions), 'true_false'
    else:
        question = random.choice(multiple_choice_questions)
        return question, 'multiple_choice'
