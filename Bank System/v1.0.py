from datetime import datetime

menu = """

[3] Depositar
[2] Sacar
[1] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
historico = []

def formatar_valor(valor):
    return f"R$ {valor:.2f}"

while True:
    opcao = input(menu)

    if opcao == "3":

        while True:
            try:
                valor = float(input("Informe o valor do depósito: ").replace(",","."))
        
                if valor > 0 and valor.is_integer():
                    saldo += valor
                    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    historico.append(f"{data_hora} - Depósito: {formatar_valor(valor)} - Subtotal: {formatar_valor(saldo)}")
                    print("Depósito realizado com sucesso!")
                    break
      
                else:
                    print("Valor inválido. Informe um valor válido.")
        
            except ValueError:
                print("Operação incorreta. Informe um comando válido.")

            repetir = input("Deseja repetir a operação? Digite: [1] Sim ou [0] Voltar ao menu: ")
        
            if repetir == "1":
                continue
        
            elif repetir == "0":
                break
        
            else: 
                print("Comando inválido. Tente novamente mais tarde.")
                exit()

    elif opcao == "2":
        
        if numero_saques >= LIMITE_SAQUES:
            print("Limite diário de saques atingido.")
            continue
        
        while True:
            try:
                valor = float(input("Informe o valor do saque: ").replace(",","."))
                if valor <= 0:
                    print("Valor inválido. Digite um valor váidado.")
        
                elif valor > limite:
                    print(f"Valor inválido. Limite de saque disponível no momento é de {formatar_valor(limite)}.")
        
                elif valor > saldo:
                    print("Saldo insuficiente.")
        
                else:
                    saldo -= valor
                    numero_saques += 1
                    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    historico.append(f"{data_hora} - Saque: -{formatar_valor(valor)} - Subtotal: {formatar_valor(saldo)}")
                    print("Saque realizado com sucesso!")
                    break

            except ValueError:
                print("Operação incorreta. Informe um comando válido.")

            repetir = input("Deseja repetir a operação? Digite: [1] Sim ou [0] Voltar ao menu: ")
        
            if repetir == "1":
                continue
        
            elif repetir == "0":
                break
        
            else: 
                print("Comando inválido. Tente novamente mais tarde.")
                exit()

    elif opcao == "1":
        print("\n================ EXTRATO ================")
        
        if not historico:
            print("SEM MOVIMENTAÇÃO")
        
        else:
            for item in historico:
                print(item)
        
        print(f"\nTOTAL EM CONTA: {formatar_valor(saldo)}")
        print("=========================================\n")

    elif opcao == "0":
        print("Obrigado pela sua participação!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
