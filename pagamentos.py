import json

ARQUIVO = "dados/pagamentos.json"

def carregar():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []

def salvar(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

def registrar_pagamento():
    pagamentos = carregar()

    nome = input("Nome do aluno: ")
    valor = float(input("Valor pago: "))

    pagamento = {
        "nome": nome,
        "valor": valor
    }

    pagamentos.append(pagamento)
    salvar(pagamentos)

    print("Pagamento registrado!")

def listar_pagamentos():
    pagamentos = carregar()

    if not pagamentos:
        print("Nenhum pagamento registrado.")
        return

    for p in pagamentos:
        print(f"{p['nome']} pagou R${p['valor']}")