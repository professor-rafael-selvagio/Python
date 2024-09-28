from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        num1 = request.form.get('num1', type=float)
        num2 = request.form.get('num2', type=float)
        operacao = request.form.get('operacao')

        if operacao == 'adição':
            resultado = num1 + num2
        elif operacao == 'subtração':
            resultado = num1 - num2
        elif operacao == 'multiplicação':
            resultado = num1 * num2
        elif operacao == 'divisão':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Erro: Divisão por zero!"

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
