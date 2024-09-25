# Inicialização de variáveis
saldo = 0  # Variável que guarda o saldo da conta
extrato = ''  # String que armazenará as movimentações (depósitos e saques)
n_saques = 0  # Contador para o número de saques realizados
LIMITE_SAQUE = 3  # Constante que define o número máximo de saques permitidos por dia
limite = 500  # Limite máximo para o valor de saque por transação

# Definição do menu a ser exibido para o usuário
menu = """
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
"""

# Loop principal que mantém o programa em execução até o usuário decidir sair
while True:
    opcao = input(menu)  # Exibe o menu e captura a opção escolhida pelo usuário
    
    # Se a opção for 'd' (depósito)
    if opcao == 'd':
        deposito = float(input('Digite o valor para depósito: '))  # Solicita o valor a ser depositado
        
        # Verifica se o valor do depósito é negativo
        if deposito < 0:
            print('Valor inválido: Tente Novamente')  # Informa erro se o valor for negativo
            continue  # Volta para o início do loop
        else:
            saldo += deposito  # Adiciona o valor depositado ao saldo
            extrato += f'Depositado o valor de R${deposito:.2f}\n'  # Registra o depósito no extrato
            
    # Se a opção for 's' (saque)
    elif opcao == 's':
        saque = float(input('Digite o valor do saque: '))  # Solicita o valor a ser sacado
        
        # Verifica se o valor do saque excede o saldo disponível
        if saque > saldo:
            print(f'Valor acima do saldo, valor disponível é de R${saldo:.2f}')  # Informa o erro
            continue  # Volta para o início do loop
        # Verifica se o valor do saque excede o limite máximo de saque por transação
        elif saque > limite:
            print('Valor acima do limite de Saque! tente novamente\n')  # Informa o erro
        # Verifica se o número de saques já atingiu o limite diário
        elif n_saques >= LIMITE_SAQUE:
            print('Limite de saques atingido! \n')  # Informa o erro
            continue  # Volta para o início do loop
        # Verifica se o valor do saque é inválido (igual ou menor que zero)
        elif saque <= 0:
            print('Valor inválido , tente novamente \n')  # Informa o erro
            continue  # Volta para o início do loop
        # Se todas as verificações estiverem corretas, o saque é permitido
        else:
            saldo -= saque  # Subtrai o valor do saque do saldo
            n_saques += 1  # Incrementa o número de saques realizados
            extrato += f'Saque realizado no valor de R${saque:.2f}\n'  # Registra o saque no extrato
            print(f'Saque realizado no valor de R${saque:.2f}\n')  # Confirma o saque para o usuário
            
    # Se a opção for 'e' (extrato)
    elif opcao == 'e':
        print('############################## EXTRATO ##############################')  # Cabeçalho do extrato
        # Verifica se houve movimentações na conta
        if extrato == '':
            print('Não foram realizadas movimentações de saque e depósito nessa conta \n')  # Informa se não houve movimentações
        else:
            print(f'{extrato} \nSaldo disponível R${saldo:.2f}\n')  # Exibe o extrato e o saldo disponível
            
    # Se a opção for 'q' (sair)
    elif opcao == 'q':
        break  # Sai do loop e encerra o programa
    
    # Se o usuário inserir uma opção inválida
    else:
        print('Insira uma opção válida: ')  # Informa o erro
        continue  # Volta para o início do loop
