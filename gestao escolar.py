import sqlite3

# Conexão com o banco de dados SQLite
conn = sqlite3.connect("gestao_escolar.db")
cursor = conn.cursor()

# Criação das tabelas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Alunos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        matricula TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cursos (
        id INTEGER PRIMARY KEY,
        nome TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Disciplinas (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        curso_id INTEGER,
        FOREIGN KEY (curso_id) REFERENCES Cursos (id)
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Professores (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        matricula TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Notas (
        id INTEGER PRIMARY KEY,
        aluno_id INTEGER,
        disciplina_id INTEGER,
        nota REAL,
        FOREIGN KEY (aluno_id) REFERENCES Alunos (id),
        FOREIGN KEY (disciplina_id) REFERENCES Disciplinas (id)
    )
""")
conn.commit()

# Funções para adicionar dados
def adicionar_aluno(nome, matricula):
    cursor.execute("INSERT INTO Alunos (nome, matricula) VALUES (?, ?)", (nome, matricula))
    conn.commit()

def adicionar_curso(nome):
    cursor.execute("INSERT INTO Cursos (nome) VALUES (?)", (nome,))
    conn.commit()

def adicionar_disciplina(nome, curso_id):
    cursor.execute("INSERT INTO Disciplinas (nome, curso_id) VALUES (?, ?)", (nome, curso_id))
    conn.commit()

def adicionar_professor(nome, matricula):
    cursor.execute("INSERT INTO Professores (nome, matricula) VALUES (?, ?)", (nome, matricula))
    conn.commit()

def adicionar_nota(aluno_id, disciplina_id, nota):
    cursor.execute("INSERT INTO Notas (aluno_id, disciplina_id, nota) VALUES (?, ?, ?)", (aluno_id, disciplina_id, nota))
    conn.commit()

# Funções para listar dados
def listar_alunos():
    cursor.execute("SELECT * FROM Alunos")
    alunos = cursor.fetchall()
    if alunos:
        print("Lista de Alunos:")
        for aluno in alunos:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Matrícula: {aluno[2]}")
    else:
        print("Nenhum aluno encontrado.")

def listar_cursos():
    cursor.execute("SELECT * FROM Cursos")
    cursos = cursor.fetchall()
    if cursos:
        print("Lista de Cursos:")
        for curso in cursos:
            print(f"ID: {curso[0]}, Nome do Curso: {curso[1]}")
    else:
        print("Nenhum curso encontrado.")

def listar_disciplinas():
    cursor.execute("SELECT D.id, D.nome, C.nome FROM Disciplinas D, Cursos C WHERE D.curso_id = C.id")
    disciplinas = cursor.fetchall()
    if disciplinas:
        print("Lista de Disciplinas:")
        for disciplina in disciplinas:
            print(f"ID: {disciplina[0]}, Nome da Disciplina: {disciplina[1]}, Curso: {disciplina[2]}")
    else:
        print("Nenhuma disciplina encontrada.")

def listar_professores():
    cursor.execute("SELECT * FROM Professores")
    professores = cursor.fetchall()
    if professores:
        print("Lista de Professores:")
        for professor in professores:
            print(f"ID: {professor[0]}, Nome: {professor[1]}, Matrícula: {professor[2]}")
    else:
        print("Nenhum professor encontrado.")

def listar_notas():
    cursor.execute("SELECT * FROM Notas")
    notas = cursor.fetchall()
    if notas:
        print("Lista de Notas:")
        for nota in notas:
            print(f"ID: {nota[0]}, Aluno ID: {nota[1]}, Disciplina ID: {nota[2]}, Nota: {nota[3]}")
    else:
        print("Nenhuma nota encontrada.")

# Funções interativas
def adicionar_aluno_interativo():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")
    adicionar_aluno(nome, matricula)
    print("Aluno adicionado com sucesso.")

def adicionar_curso_interativo():
    nome = input("Digite o nome do curso: ")
    adicionar_curso(nome)
    print("Curso adicionado com sucesso.")

def adicionar_disciplina_interativo():
    nome = input("Digite o nome da disciplina: ")
    print("Cursos disponíveis:")
    cursos = cursor.execute("SELECT * FROM Cursos").fetchall()
    for curso in cursos:
        print(f"{curso[0]}. {curso[1]}")
    curso_id = int(input("Digite o ID do curso para a disciplina: "))
    adicionar_disciplina(nome, curso_id)
    print("Disciplina adicionada com sucesso.")

def adicionar_professor_interativo():
    nome = input("Digite o nome do professor: ")
    matricula = input("Digite a matrícula do professor: ")
    adicionar_professor(nome, matricula)
    print("Professor adicionado com sucesso.")

def adicionar_nota_interativo():
    aluno_id = int(input("Digite o ID do aluno: "))
    disciplina_id = int(input("Digite o ID da disciplina: "))
    nota = float(input("Digite a nota: "))
    adicionar_nota(aluno_id, disciplina_id, nota)
    print("Nota adicionada com sucesso.")

def excluir_aluno(id_aluno):
    cursor.execute("DELETE FROM Alunos WHERE id = ?", (id_aluno,))
    conn.commit()
    print(f"Aluno com ID {id_aluno} excluído com sucesso.")

def alterar_aluno(id_aluno, novo_nome, nova_matricula):
    cursor.execute("UPDATE Alunos SET nome = ?, matricula = ? WHERE id = ?", (novo_nome, nova_matricula, id_aluno))
    conn.commit()
    print(f"Informações do aluno com ID {id_aluno} alteradas com sucesso.")


# Função principal
def main():
    while True:
        print("\nOpções:")
        print("1. Adicionar aluno")
        print("2. Adicionar curso")
        print("3. Adicionar disciplina")
        print("4. Adicionar professor")
        print("5. Adicionar nota")
        print("6. Listar alunos")
        print("7. Listar cursos")
        print("8. Listar disciplinas")
        print("9. Listar professores")
        print("10. Listar notas")
        print("11. Excluir aluno")
        print("12. Alterar aluno")
        print("13. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_aluno_interativo()
        elif opcao == '2':
            adicionar_curso_interativo()
        elif opcao == '3':
            adicionar_disciplina_interativo()
        elif opcao == '4':
            adicionar_professor_interativo()
        elif opcao == '5':
            adicionar_nota_interativo()
        elif opcao == '6':
            listar_alunos()
        elif opcao == '7':
            listar_cursos()
        elif opcao == '8':
            listar_disciplinas()
        elif opcao == '9':
            listar_professores()
        elif opcao == '10':
            listar_notas()
        elif opcao == '11':
            id_aluno = int(input("Digite o ID do aluno que deseja excluir: "))
            excluir_aluno(id_aluno)
        elif opcao == '12':
            id_aluno = int(input("Digite o ID do aluno que deseja alterar: "))
            novo_nome = input("Digite o novo nome do aluno: ")
            nova_matricula = input("Digite a nova matrícula do aluno: ")
            alterar_aluno(id_aluno, novo_nome, nova_matricula)
        elif opcao == '13':
            break
        else:
         print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()