import mysql.connector
from mysql.connector import errorcode

print('Conectando...')
try:
    conn = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = 'damonts210'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")

cursor.execute("CREATE DATABASE `jogoteca`;")

cursor.execute("USE `jogoteca`;")

# criando tabelas
TABLES = {}
TABLES['Jogos'] = ('''
      CREATE TABLE `jogo` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `nome` varchar(50) NOT NULL,
        `categoria` varchar(40) NOT NULL,
        `console` varchar(20) NOT NULL,
        PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
        `nome` varchar(20) NOT NULL,
        `nickname` varchar(8) NOT NULL,
        `senha` varchar(100) NOT NULL,
        PRIMARY KEY (`nickname`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print(f'Criando tabela {tabela_nome}')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já existe')
        else:
            print(err.msg)
    else:
        print('OK')

# inserindo usuarios
usuario_sql = "INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)"
usuarios = [
    ("Daniel Montanari", "damont", "1234"),
    ("Vinicius Gabriel", "pantero", "1234"),
    ("Tamara Zoner", "tzoner", "1234")
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('SELECT * FROM jogoteca.usuarios')
print(' ---------- Usuários: ---------- ')
for user in cursor.fetchall():
    print(user[1])


# inserindo jogos
jogos_sql = "INSERT INTO jogo (id, nome, categoria, console) VALUES (DEFAULT, %s, %s, %s)"
jogos = [
    ("Tetris", "Puzzle", "Atari"),
    ("League of Legends", "Moba", "PC"),
    ("Counter Strike", "FPS", "PC")
]
cursor.executemany(jogos_sql, jogos)

cursor.execute('SELECT * FROM jogoteca.jogo')
print(' ---------- Usuários: ---------- ')
for user in cursor.fetchall():
    print(user[1])