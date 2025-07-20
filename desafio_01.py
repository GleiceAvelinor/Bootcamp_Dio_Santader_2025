#Criar um sistema bancário com as operações:sacar, depositar e visualisar extrato

versão = '1.0.0'
AUTOR = 'DIO-SANTANDER' 'Desenvolvedora: Gleice Avelino'



def menu():
    print('''\n
    ========== BANCO DIO-SANTANDER ==========
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
    ==========================
    ''')
    return input('Escolha uma opção: ').lower()

LIMITE_SAQUE = 500.00
SAQUE_DIARIO = 3
saldo = 0.00
extrato = []


while True:
        opcao = menu()
        if opcao == '1':
            valor = float(input('Informe o valor a ser depositado: '))
            if valor > 0:
                saldo += valor
                extrato.append(f'Depósito: R$ {valor:.2f}')
                print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
            else:
                print('Valor inválido para depósito.')
        elif opcao == '2':
            valor = float(input('Informe o valor a ser sacado: '))
            if 0 < valor <= LIMITE_SAQUE and valor <= saldo:
                saldo -= valor
                extrato.append(f'Saque: R$ {valor:.2f}')
                print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
            elif valor > LIMITE_SAQUE:
                print(f'Saque inválido. O valor máximo para saque é R$ {LIMITE_SAQUE:.2f}.')
            else:
                print('Saque inválido. Verifique o limite ou saldo disponível.')
        elif opcao == '3':
            print('\nExtrato:')
            if extrato:
                for transacao in extrato:
                    print(transacao)
            else:   
                print('Nenhuma transação realizada.')
            print(f'Saldo atual: R$ {saldo:.2f}')   






if __name__ == "__main__":  
    # Inicie o programa chamando o loop principal (já está rodando acima)
    pass
    