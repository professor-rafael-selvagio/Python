from flask import Flask
from routes.aluno_routes import aluno_bp
from routes.whatsapp_routes import whatsapp_bp
from routes.faker_routes import faker_bp

app = Flask(__name__)

# Registro das rotas
app.register_blueprint(aluno_bp)
app.register_blueprint(whatsapp_bp)
app.register_blueprint(faker_bp)


if __name__ == '__main__':
    app.run(debug=True)
