import json

ARQUIVO = "dados/alunos.json"

def carregar():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []

def salvar(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

def cadastrar_aluno():
    alunos = carregar()

    nome = input("Nome: ")
    idade = input("Idade: ")
    plano = input("Plano: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "plano": plano
    }

    alunos.append(aluno)
    salvar(alunos)

    print("Aluno cadastrado!")

def listar_alunos():
    alunos = carregar()

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for i, aluno in enumerate(alunos, 1):
        print(f"{i}. {aluno['nome']} - {aluno['plano']}")