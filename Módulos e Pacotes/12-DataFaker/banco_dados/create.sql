-- 1. Criar o banco de dados
CREATE DATABASE PlataformaStreamingJogos;
USE PlataformaStreamingJogos;

-- 2. Tabela Jogos
CREATE TABLE Jogos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    desenvolvedor VARCHAR(100) NOT NULL,
    genero VARCHAR(50)
);

-- 3. Tabela Usuarios
CREATE TABLE Usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    data_registro DATE NOT NULL
);

-- 4. Tabela Transmissoes
CREATE TABLE Transmissoes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    jogo_id INT NOT NULL,
    data_transmissao DATETIME NOT NULL,
    visualizacoes INT DEFAULT 0,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id),
    FOREIGN KEY (jogo_id) REFERENCES Jogos(id)
);

-- 5. Tabela Comentarios
CREATE TABLE Comentarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    transmissao_id INT NOT NULL,
    usuario_id INT NOT NULL,
    comentario TEXT NOT NULL,
    data_comentario DATETIME NOT NULL,
    FOREIGN KEY (transmissao_id) REFERENCES Transmissoes(id),
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
);
