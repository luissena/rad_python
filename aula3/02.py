import os

# Função para cadastrar um novo aluno
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    curso = input("Digite o curso do aluno: ")

    # Verifica se o arquivo de alunos já existe
    if not os.path.exists("alunos.txt"):
        with open("alunos.txt", "w") as arquivo:
            arquivo.write("Nome;Email;Curso\n")

    # Abre o arquivo no modo de escrita para adicionar o novo aluno
    with open("alunos.txt", "a") as arquivo:
        arquivo.write(f"{nome};{email};{curso}\n")

    print("Aluno cadastrado com sucesso!")

# Função para listar todos os alunos cadastrados
def listar_alunos():
    if os.path.exists("alunos.txt"):
        with open("alunos.txt", "r") as arquivo:
            primeiro = True  # Variável para controlar a impressão do cabeçalho
            for linha in arquivo:
                if primeiro:
                    primeiro = False
                    continue  # Pula a primeira linha (cabeçalho)
                nome, email, curso = linha.strip().split(";")
                print(f"Nome: {nome}, Email: {email}, Curso: {curso}")
    else:
        print("Nenhum aluno cadastrado.")

# Função para buscar um aluno pelo nome
def buscar_aluno():
    nome_busca = input("Digite o nome do aluno que deseja buscar: ")
    encontrado = False

    if os.path.exists("alunos.txt"):
        with open("alunos.txt", "r") as arquivo:
            for linha in arquivo:
                nome, email, curso = linha.strip().split(";")
                if nome_busca.lower() in nome.lower():
                    print(f"Nome: {nome}, Email: {email}, Curso: {curso}")
                    encontrado = True

    if not encontrado:
        print("Aluno não encontrado.")

# Loop principal do programa
while True:
    print("\nOpções:")
    print("1. Cadastrar um novo aluno")
    print("2. Listar os alunos cadastrados")
    print("3. Buscar um aluno pelo nome")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        buscar_aluno()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")