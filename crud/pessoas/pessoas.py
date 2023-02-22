# Criando o Banco de Dados
import sqlite3

conn = sqlite3.connect('pessoas.db')

cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE pessoas (
    nome TEXT NOT NULL,
    idade INTEGER,
    endereco TEXT,
    cidade TEXT,
    estado TEXT,
    profissao TEXT
);
""")

print("Tabela criada com sucesso!")

conn.close()

# Menu
while True:
    print("="*40)
    print("MENU:")
    print("1 - Criar registro")
    print("2 - Consultar registro")
    print("3 - Atualizar registro")
    print("4 - Deletar registro")
    print("0 - Sair")
    print("="*40)
    opcao = int(input("Digite a opção desejada: "))

    # Criar
    if opcao == 1:
        conn = sqlite3.connect('pessoas.db')
        cursor = conn.cursor()
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        endereco = input("Digite o endereço: ")
        cidade = input("Digite a cidade: ")
        estado = input("Digite o estado: ")
        profissao = input("Digite a profissão: ")
        cursor.execute("""
        INSERT INTO pessoas (nome, idade, endereco, cidade, estado, profissao)
        VALUES (?,?,?,?,?,?)
        """, (nome, idade, endereco, cidade, estado, profissao))
        conn.commit()
        print("Registro criado com sucesso!")
        conn.close()

    # Consultar
    elif opcao == 2:
        conn = sqlite3.connect('pessoas.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM pessoas;
        """)
        for linha in cursor.fetchall():
            print(linha)
        conn.close()

    # Atualizar
    elif opcao == 3:
        conn = sqlite3.connect('pessoas.db')
        cursor = conn.cursor()
        nome = input("Digite o nome para atualizar o registro: ")
        idade = int(input("Digite a nova idade: "))
        endereco = input("Digite o novo endereço: ")
        cidade = input("Digite a nova cidade: ")
        estado = input("Digite o novo estado: ")
        profissao = input("Digite a nova profissão: ")
        cursor.execute("""
        UPDATE pessoas
        SET idade = ?, endereco = ?, cidade = ?, estado = ?, profissao = ?
        WHERE nome = ?
        """, (idade, endereco, cidade, estado, profissao, nome))
        conn.commit()
        print("Registro atualizado com sucesso!")
        conn.close()

    # Deletar
    elif opcao == 4:
        conn = sqlite3.connect('pessoas.db')
        cursor = conn.cursor()
        nome = input("Digite o nome para deletar o registro: ")
        cursor.execute("""
        DELETE FROM pessoas
        WHERE nome = ?
        """, (nome,))
        conn.commit()
        print("Registro deletado com sucesso!")
        conn.close()

    # Sair
    elif opcao == 0:
        break

    else:
        print("Opção Inválida!")