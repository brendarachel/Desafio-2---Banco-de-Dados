#Banco de Dados
import sqlite3

exercicio2 = sqlite3.connect('db.exercicio')
cursor = exercicio2.cursor()

#5. Criar uma Tabela e Inserir dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária),
#nome (texto), idade (inteiro) e saldo (float). Insira alguns registros
#de clientes na tabela.
cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')

cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Brenda", 29, 5000)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Vitória", 18, 1000)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Sofia", 19, 500)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "Yago", 31, 4000)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5, "Yuri", 28, 900)')


#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
for cliente in dados:
    print(cliente)
print()

#b) Calcule o saldo médio dos clientes.
dados = cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')
for cliente in dados:
    print(cliente)
print()

#c) Encontre o cliente com o saldo máximo.
dados = cursor.execute('SELECT nome, MAX(saldo) AS saldo_maximo FROM clientes')
for cliente in dados:
    print(cliente)
print()

#d) Conte quantos clientes têm saldo acima de 1000.
dados = cursor.execute('SELECT COUNT(id) FROM clientes WHERE saldo > 1000')
for cliente in dados:
    print(cliente)
print()

#7. Atualização e Remoção com condições
#a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo="1500" WHERE id="5"')
dados = cursor.execute('SELECT * FROM clientes')
for cliente in dados:
    print(cliente)
print()

#b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes WHERE id="1"')
dados = cursor.execute('SELECT * FROM clientes')
for cliente in dados:
    print(cliente)
print()

#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária),
#cliente_id (chave estrangeira referenciando o id da tabela "clientes"),
#produto (texto) e valor (real). Insira algumas compras associadas a clientes
#existentes na tabela "clientes". Escreva uma consulta para exibir o nome do
#cliente, o produto e o valor de cada compra.

#Criação da tabela
cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(250), valor FLOAT, CONSTRAINT fk_clientes FOREIGN KEY (cliente_id) REFERENCES clientes(id))')

#Inserção de dados
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (6, 1, "computador", 4000)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (7, 2, "fone de ouvido", 100)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (8, 3, "sapato", 50)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (9, 4, "smartphone", 3000)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (10, 5, "livro", 60)')

#Consulta
dados = cursor.execute('SELECT c.nome, co.produto, co.valor FROM clientes c INNER JOIN compras co ON c.id=co.cliente_id')
print('Nome do Cliente | Produto | Valor da Compra')
for i in dados:
    print(f'{i[0]} | {i[1]} | R${i[2]:.2f}')


exercicio2.commit()
exercicio2.close