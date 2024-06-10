menu = '''




[d] depisitar

[s] sacar

[e] extrato

[q] sair




=> '''




saldo = 0

limite = 500

extrato_deposito = []

extrato_saque = []

numero_saques = 0

LIMITE_SAQUE = 3

opcao = input(menu)




def deposito(valor_deposito):

     valor_deposito

     extrato_deposito.append(valor_deposito)

     return valor_deposito




def saque(valor_saque, LIMITE_SAQUE, saldo):

     if valor_saque <= saldo and valor_saque <= limite:

            if LIMITE_SAQUE != 0:

                saldo -= valor_saque

                extrato_saque.append(valor_saque)

     else:

         print("\nlimite de saque atingido ou saldo infulficiente!")

     return saldo




while opcao != "q":

    if opcao == "d":

        valor_deposito = int(input('Digite o valor do deposito:'))

        if valor_deposito > 0:

          saldo += deposito(valor_deposito)

          opcao = input(menu)

    

    if opcao == "s":

        valor_saque = int(input('Digite o valor do saque: \n'))

        saldo =  saque(valor_saque,LIMITE_SAQUE,saldo)

        LIMITE_SAQUE -= 1

        numero_saques += 1

        controle = numero_saques

        opcao = input(menu)

       

    

    if opcao == "e":

        for i in range(len(extrato_deposito)):

            for j  in range(numero_saques):

                if controle > 0:

                    print('Saque feito no valor de:')

                    print(extrato_saque[j])

                    controle -= 1

        

            print('deposito feito no valor de: ')

            print(extrato_deposito[i])

        opcao = input(menu)
