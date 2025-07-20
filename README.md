# Bootcamp_Dio_Santader_2025
#Criar um sistema bancário com as operações:sacar, depositar e visualisar extrato
Descrição do Projeto: Sistema Bancário Simples
Este projeto é a implementação de um sistema bancário básico desenvolvido em Python. Ele simula as operações fundamentais de uma conta corrente, permitindo que o usuário realize três ações principais: depositar, sacar e visualizar um extrato das transações.

Funcionalidades Implementadas:
Menu Interativo: Apresenta um menu claro e fácil de usar, guiando o usuário pelas opções disponíveis (depositar, sacar, extrato, sair).

Depósito:

Permite ao usuário adicionar fundos à sua conta.

Valida se o valor do depósito é positivo, garantindo que apenas quantias válidas sejam adicionadas ao saldo.

Registra cada depósito no histórico do extrato.

Saque:

Permite ao usuário retirar fundos da sua conta.

Inclui validações importantes:

Verifica se o valor do saque é positivo.

Impede saques que excedam um limite máximo por operação (atualmente R$ 500,00).

Assegura que o usuário possua saldo suficiente para cobrir o valor do saque.

Registra cada saque no histórico do extrato.

Extrato:

Exibe um histórico detalhado de todas as transações (depósitos e saques) realizadas na conta.

Informa claramente o saldo atual da conta após todas as operações.

Notifica o usuário se ainda não houve nenhuma transação.

Saída do Sistema: Permite que o usuário encerre o programa de forma organizada.

Como Funciona:
O sistema opera em um loop contínuo, exibindo o menu e processando a escolha do usuário até que a opção de sair seja selecionada. O saldo da conta e o histórico de transações são mantidos em variáveis simples (um número para o saldo e uma lista para o extrato) enquanto o programa está em execução.

Propósito:
O objetivo deste projeto é demonstrar a lógica básica por trás de um sistema bancário, utilizando conceitos fundamentais de programação como:

Funções: Para organizar o código e reutilizar partes dele (ex: a função menu).

Variáveis: Para armazenar dados como saldo, limites e histórico.

Estruturas Condicionais (if/elif/else): Para tomar decisões baseadas nas escolhas do usuário e nas regras de negócio (ex: verificar saldo antes de sacar).

Loops (while): Para manter o sistema em funcionamento contínuo.

Listas: Para armazenar o histórico de transações (extrato).
