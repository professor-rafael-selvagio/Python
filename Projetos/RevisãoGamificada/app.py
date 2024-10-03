from flask import Flask, render_template, request, jsonify, redirect, url_for
from questions import multiple_choice_questions, true_false_questions

app = Flask(__name__)

# Inicializa o estado do quiz
quiz_state = {
    'current_question_index': 0,
    'questions': multiple_choice_questions + true_false_questions,
}

def get_question(index):
    total_questions = len(quiz_state['questions'])

    # Verifica se o índice atual está dentro do intervalo
    if index < total_questions:
        return quiz_state['questions'][index]
    else:
        return None  # Retorna None se o índice estiver fora do intervalo
    
@app.route('/next_question', methods=['GET'])
def next_question():
    quiz_state['current_question_index'] += 1
    current_question_index = quiz_state['current_question_index']
    
    if current_question_index < len(quiz_state['questions']):
        return render_template('index.html', 
                               question=quiz_state['questions'][current_question_index],
                               feedback=None, 
                               show_next_button=False, 
                               question_number=current_question_index + 1)
    else:
        return redirect(url_for('result'))  # ou para onde deseja redirecionar após o final


@app.route('/')
def index():
    # Reinicia o quiz quando o usuário acessa a página inicial
    quiz_state['current_question_index'] = 0

    return render_template('index.html', question=get_question(0), feedback='', show_next_button=False, question_number=1)

@app.route('/submit', methods=['POST'])
def submit():
    answer = request.form.get('answer')
    current_question_index = quiz_state['current_question_index']
    correct_answer = quiz_state['questions'][current_question_index]['answer']
    
    if answer == correct_answer:
        feedback = "Resposta correta!"
    else:
        feedback = f"Resposta incorreta! A resposta correta é: {correct_answer}"
    
    # Checa se há uma próxima pergunta
    if current_question_index + 1 < len(quiz_state['questions']):
        show_next_button = True
    else:
        show_next_button = False

    # Retorna o feedback e a pergunta atual como um JSON
    return jsonify({
        'feedback': feedback,
        'question': quiz_state['questions'][current_question_index],
        'question_number': current_question_index + 1,
        'show_next_button': show_next_button  # Inclui a variável no JSON
    })

@app.route('/result')
def result():
    # Supondo que você tenha um dicionário ou lista que armazena as perguntas e as respostas
    # Exemplo de estrutura:
    # quiz_state = {
    #     'questions': [
    #         {'question': 'Qual é a capital da França?', 'answer': 'Paris'},
    #         {'question': '2 + 2 é igual a 4?', 'answer': 'True'},
    #         # ...
    #     ],
    #     'user_answers': ['Paris', 'False', ...]  # Respostas do usuário
    # }

    questions = quiz_state['questions']
    user_answers = quiz_state.get('user_answers', [])
    
    # Calcula a pontuação
    score = sum(1 for i in range(len(questions)) if user_answers[i] == questions[i]['answer'])
    total_questions = len(questions)
    
    # Prepare os dados para o resultado
    results = []
    for question, user_answer in zip(questions, user_answers):
        correct_answer = question['answer']
        results.append((question['question'], user_answer, correct_answer))

    return render_template('result.html', score=score, total_questions=total_questions, results=results)



if __name__ == '__main__':
    app.run(debug=True)
