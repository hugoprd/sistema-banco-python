saldo = 0;
limite = 500;
extrato = "";
numero_saques = 0;
LIMITE_SAQUES = 3;

def saldoF():
    global saldo;

    print(f"Seu saldo eh de R${saldo:.2f}\n");

def saque(valorS):
    global saldo, extrato;

    saldo -= valorS;
    extrato += f"Saque: R${valorS:.2f}\n";

    print(f"R${valorS:.2f} sacado(s).\n");

def deposito(valorD):
    global saldo, extrato;

    saldo += valorD;
    extrato += f"Deposito: R${valorD:.2f}\n";

    print(f"R${valorD:.2f} depositado(s).\n");

def extratoF():
    print(extrato);
    print(f"Saldo: {saldo:.2f}");

print_menu = """
    ==============================||==============================
    Bem vindo ao Sistema Bancário. Por favor, escolha uma opção...
    [1] Saldo
    [2] Sacar
    [3] Depositar
    [4] Extrato
    [5] Sair

    => 
"""

while True:
    resposta = int(input(print_menu));

    if resposta == 1:
        saldoF();
    elif resposta == 2:
        resp = int(input("[1] Saque\n[2] Voltar\n=> "));
        if resp == 1:
            print(f"Quantidade(s) de saques diarios restantes: {LIMITE_SAQUES - numero_saques}\n");
            valorS = float(input("Valor do saque: "));
            if valorS > 500:
                print("O limite pra sacar, por vez, eh de R$500.00. Tente novamente...\n");
            elif valorS <= 0:
                print("Valor invalido. Tente novamente...\n");
            elif saldo <= 0:
                print("Impossivel sacar por falta de saldo. Tente novamente...\n");
            elif numero_saques >= LIMITE_SAQUES:
                print("Chegou ao limite de saques diarios. Tente novamente amanha...\n");
            elif valorS > saldo:
                print("Voce nao pode retirar mais dinheiro do que possui no banco. Tente novamente...\n");
            else:
                saque(valorS);
                numero_saques += 1;
        else:
            print("Resposta invalida! Tente novamente...\n");
    elif resposta == 3:
        resp = int(input("[1] Deposito\n[2] Voltar\n=> "));
        if resp == 1:
            valorD = float(input("Valor do deposito: "));
            deposito(valorD);
        else:
            print("Voltando...\n");
    elif resposta == 4:
        resp = int(input("[1] Ver extrato\n[2] Voltar\n=> "));
        if resp == 1:
            if extrato != "":
                extratoF();
            else:
                print("Nao foram realizadas movimentacoes! Tente novamente...\n");
        else:
            print("Voltando...\n");
    elif resposta == 5:
        print("\nSaindo do programa...\n");
        break;
    else:
        print("Resposta invalida! Tente novamente...\n");