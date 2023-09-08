#Banco de Dados
import sqlite3

exercicio = sqlite3.connect('db.exercicio')
cursor = exercicio.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro),
#nome (texto), idade (inteiro) e curso (texto).
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(250))')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no
#exercicio anterior.
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Brenda", 29, "TI")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Vitória", 18, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Sofia", 19, "Medicina")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Yago", 31, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Yuri", 28, "Direito")')

#3. Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
dados = cursor.execute('SELECT * FROM alunos')
for aluno in dados:
    print(aluno)
print()

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
for aluno in dados:
    print(aluno)
print()

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados = cursor.execute('SELECT nome FROM alunos WHERE curso="Engenharia" ORDER BY nome')
for aluno in dados:
    print(aluno)
print()

#d) Contar o número total de alunos na tabela.
dados = cursor.execute('SELECT COUNT(*) FROM alunos')
for aluno in dados:
    print(f'Número total de alunos: {aluno}')
print()

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
dados = cursor.execute('UPDATE alunos SET idade=30 WHERE id=4')
dados = cursor.execute('SELECT * FROM alunos')
for aluno in dados:
    print(aluno)
print()

#b) Remova um aluno pelo seu ID.
dados = cursor.execute('DELETE FROM alunos WHERE id=5')
dados = cursor.execute('SELECT * FROM alunos')
for aluno in dados:
    print(aluno)
print()

exercicio.commit()
exercicio.close