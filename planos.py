import json

ARQUIVO = "dados/planos.json"

def carregar():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []

def salvar(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

def cadastrar_plano():
    planos = carregar()

    nome = input("Nome do plano: ")
    valor = float(input("Valor: "))
    duracao = input("Duração (ex: mensal): ")

    plano = {
        "nome": nome,
        "valor": valor,
        "duracao": duracao
    }

    planos.append(plano)
    salvar(planos)

    print("Plano cadastrado!")

def listar_planos():
    planos = carregar()

    if not planos:
        print("Nenhum plano cadastrado.")
        return

    for i, plano in enumerate(planos, 1):
        print(f"{i}. {plano['nome']} - R${plano['valor']} ({plano['duracao']})")