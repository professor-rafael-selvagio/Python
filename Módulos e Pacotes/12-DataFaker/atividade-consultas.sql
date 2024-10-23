-- 1. Listar todos os jogos com seus desenvolvedores e gêneros.
SELECT * FROM Jogos;

-- 2. Contar quantos usuários existem no sistema.
SELECT COUNT(*) AS total_usuarios FROM Usuarios;

-- 3. Listar todas as transmissões, incluindo o nome do usuário que as fez.
SELECT Transmissoes.*, Usuarios.nome AS usuario_nome 
FROM Transmissoes 
INNER JOIN Usuarios ON Transmissoes.usuario_id = Usuarios.id;

-- 4. Encontrar a média de visualizações por transmissão.
SELECT AVG(visualizacoes) AS media_visualizacoes FROM Transmissoes;

-- 5. Listar todos os comentários feitos em transmissões específicas, incluindo o nome do jogo.
SELECT Comentarios.comentario, Jogos.titulo AS jogo_titulo 
FROM Comentarios 
INNER JOIN Transmissoes ON Comentarios.transmissao_id = Transmissoes.id 
INNER JOIN Jogos ON Transmissoes.jogo_id = Jogos.id;

-- 6. Listar jogos com mais de 500 visualizações em suas transmissões.
SELECT Jogos.titulo, Transmissoes.visualizacoes 
FROM Jogos 
INNER JOIN Transmissoes ON Jogos.id = Transmissoes.jogo_id 
WHERE Transmissoes.visualizacoes > 500;

-- 7. Listar usuários e o número de transmissões que fizeram.
SELECT Usuarios.nome AS usuario_nome, COUNT(Transmissoes.id) AS total_transmissoes 
FROM Usuarios 
LEFT JOIN Transmissoes ON Usuarios.id = Transmissoes.usuario_id 
GROUP BY Usuarios.id;

-- 8. Encontrar todos os comentários de um usuário específico.
SELECT Comentarios.comentario 
FROM Comentarios 
INNER JOIN Usuarios ON Comentarios.usuario_id = Usuarios.id 
WHERE Usuarios.nome = 'Emanuelly Costa';  -- Substitua 'Nome do Usuario' pelo nome desejado

-- 9. Listar todos os jogos e suas respectivas transmissões.
SELECT Jogos.titulo, Transmissoes.data_transmissao 
FROM Jogos 
INNER JOIN Transmissoes ON Jogos.id = Transmissoes.jogo_id;

-- 10. Listar jogos e a quantidade de comentários feitos em cada um.
SELECT Jogos.titulo AS jogo_titulo, COUNT(Comentarios.id) AS total_comentarios 
FROM Jogos 
LEFT JOIN Transmissoes ON Jogos.id = Transmissoes.jogo_id 
LEFT JOIN Comentarios ON Transmissoes.id = Comentarios.transmissao_id 
GROUP BY Jogos.id;

-- 11. Listar todos os comentários junto com o nome do usuário que os fez e o título da transmissão relacionada.
SELECT Comentarios.comentario, Usuarios.nome AS usuario_nome, Transmissoes.data_transmissao, Transmissoes.visualizacoes 
FROM Comentarios 
INNER JOIN Usuarios ON Comentarios.usuario_id = Usuarios.id 
INNER JOIN Transmissoes ON Comentarios.transmissao_id = Transmissoes.id;

-- 12. Encontrar todos os usuários e suas transmissões, incluindo a data da transmissão.
SELECT Usuarios.nome AS usuario_nome, Transmissoes.data_transmissao 
FROM Usuarios 
INNER JOIN Transmissoes ON Usuarios.id = Transmissoes.usuario_id;

-- 13. Listar todos os jogos e suas respectivas transmissões, mostrando também o número de visualizações.
SELECT Jogos.titulo AS jogo_titulo, Transmissoes.data_transmissao, Transmissoes.visualizacoes 
FROM Jogos 
INNER JOIN Transmissoes ON Jogos.id = Transmissoes.jogo_id;

-- 14. Encontrar todos os jogos e os comentários feitos sobre eles, incluindo o nome do usuário que fez o comentário.
SELECT Jogos.titulo AS jogo_titulo, Comentarios.comentario, Usuarios.nome AS usuario_nome 
FROM Jogos 
INNER JOIN Transmissoes ON Jogos.id = Transmissoes.jogo_id 
INNER JOIN Comentarios ON Transmissoes.id = Comentarios.transmissao_id 
INNER JOIN Usuarios ON Comentarios.usuario_id = Usuarios.id;

-- 15. Listar os jogos, suas transmissões e o número de comentários feitos em cada transmissão.
SELECT Jogos.titulo AS jogo_titulo, Transmissoes.data_transmissao, COUNT(Comentarios.id) AS total_comentarios 
FROM Jogos 
INNER JOIN Transmissoes ON Jogos.id = Transmissoes.jogo_id 
LEFT JOIN Comentarios ON Transmissoes.id = Comentarios.transmissao_id 
GROUP BY Transmissoes.id;
