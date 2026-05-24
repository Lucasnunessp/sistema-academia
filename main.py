from alunos import cadastrar_aluno, listar_alunos
from planos import cadastrar_plano, listar_planos
from pagamentos import registrar_pagamento, listar_pagamentos

import os
import time
import sys

def digitar(texto, velocidade=0.02):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def inicializacao():
    limpar_tela()
    digitar("Inicializando sistema...", 0.03)
    time.sleep(0.5)
    digitar("Carregando dados...", 0.03)
    time.sleep(0.5)
    digitar("Sistema pronto!", 0.03)
    time.sleep(1)

def menu():
    while True:
        limpar_tela()

        print("\n" + "="*35)
        digitar("🏋️ SISTEMA DE ACADEMIA", 0.02)
        print("="*35)

        digitar("📌 1 - Cadastrar aluno", 0.01)
        digitar("📋 2 - Listar alunos", 0.01)
        digitar("💳 3 - Cadastrar plano", 0.01)
        digitar("📊 4 - Listar planos", 0.01)
        digitar("💰 5 - Registrar pagamento", 0.01)
        digitar("📄 6 - Listar pagamentos", 0.01)
        digitar("❌ 0 - Sair", 0.01)

        print("="*35)

        opcao = input("\n👉 Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            cadastrar_plano()
        elif opcao == "4":
            listar_planos()
        elif opcao == "5":
            registrar_pagamento()
        elif opcao == "6":
            listar_pagamentos()
        elif opcao == "0":
            digitar("\n👋 Saindo do sistema...", 0.02)
            break
        else:
            digitar("\n⚠️ Opção inválida!", 0.02)

        input("\nPressione ENTER para continuar...")

inicializacao()
menu()
