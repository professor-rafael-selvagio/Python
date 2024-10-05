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
    },
    
    {
        "question": "No Power BI, um gráfico de pizza é usado para mostrar a variação ao longo do tempo.",
        "answer": False
    },
    {
        "question": "As funções DAX no Power BI só podem ser usadas em colunas calculadas.",
        "answer": False
    },
    {
        "question": "No Power BI, você pode criar colunas e medidas personalizadas usando DAX.",
        "answer": True
    },
    {
        "question": "O Power BI oferece suporte à criação de painéis em tempo real.",
        "answer": True
    },
    {
        "question": "A versão gratuita do Power BI possui todas as funcionalidades da versão paga.",
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
    },


    {
        "question": "Qual das seguintes funções é usada para calcular a média no Power BI?",
        "options": ["AVERAGE", "SUM", "COUNT", "MIN"],
        "answer": "AVERAGE"
    },
    {
        "question": "Qual desses gráficos NÃO é um tipo de visualização no Power BI?",
        "options": ["Gráfico de Rosca", "Gráfico de Cascata", "Gráfico de Funil", "Gráfico de Pizza 3D"],
        "answer": "Gráfico de Pizza 3D"
    },
    {
        "question": "Qual a principal função do Power Query no Power BI?",
        "options": ["Criar dashboards interativos.", "Transformar e limpar dados antes da análise.", "Publicar relatórios no Power BI Service.", "Criar relatórios financeiros complexos."],
        "answer": "Transformar e limpar dados antes da análise."
    },
    {
        "question": "Qual o nome da funcionalidade do Power BI que permite conectar várias tabelas relacionadas?",
        "options": ["Relacionamentos", "Medidas", "Colunas Calculadas", "Grupos"],
        "answer": "Relacionamentos"
    },
    {
        "question": "Em que cenário é mais útil utilizar um gráfico de linha no Power BI?",
        "options": ["Comparar categorias diferentes.", "Analisar dados ao longo do tempo.", "Visualizar uma única métrica.", "Mostrar proporções de um todo."],
        "answer": "Analisar dados ao longo do tempo."
    },
    {
        "question": "Qual destes recursos NÃO está disponível na versão gratuita do Power BI?",
        "options": ["Criação de dashboards", "Agendamento de atualização de dados", "Importação de dados do Excel", "Criação de relatórios personalizados"],
        "answer": "Agendamento de atualização de dados"
    },
    {
        "question": "Qual destes elementos é necessário para criar uma medida no Power BI?",
        "options": ["Power Query", "Funções DAX", "Relacionamentos", "Filtros"],
        "answer": "Funções DAX"
    },
    {
        "question": "O que significa a sigla 'ETL', amplamente utilizada no contexto do Power BI?",
        "options": ["Extract, Transform, Load", "Export, Test, Load", "Evaluate, Transfer, Load", "Edit, Transform, Link"],
        "answer": "Extract, Transform, Load"
    },
    {
        "question": "Qual o principal benefício de usar 'Medidas' no Power BI?",
        "options": ["Armazenar grandes quantidades de dados.", "Realizar cálculos dinâmicos em tempo de execução.", "Criar gráficos personalizados.", "Gerar relatórios em tempo real."],
        "answer": "Realizar cálculos dinâmicos em tempo de execução."
    },
    {
        "question": "Qual destes elementos NÃO pode ser utilizado em um gráfico de pizza no Power BI?",
        "options": ["Categoria", "Legenda", "Valor", "Título Interativo"],
        "answer": "Título Interativo"
    }
]

def get_random_question():
    """Retorna uma pergunta aleatória (pode ser verdadeiro/falso ou múltipla escolha)."""
    if random.choice([True, False]):  # Decide aleatoriamente entre as duas categorias
        return random.choice(true_false_questions), 'true_false'
    else:
        question = random.choice(multiple_choice_questions)
        return question, 'multiple_choice'
