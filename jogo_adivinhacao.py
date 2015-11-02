from random import randint

jogar = 1       #Enquanto jogar=1 o jogo rodara novamente.
recorde = 100   #Recorde atual.

while(jogar == 1):
    sorteio = randint(1,100)
    num = 0         #Resetando numero informado pelo usuario.
    tentativas = 1  #Resetando quantidade de jogadas realizadas.
    
    print("\nO Computador sorteou um Numero entre 1 e 100!\nTente adivinha-lo!\n")

    while(num != sorteio):
        num = int(input("Informe um Numero: "))
        if(num == sorteio):
            print("\nParabens! Voce Ganhou!")
            print("Total de Tentativas: %i" %tentativas)
            if(tentativas < recorde):
                recorde = tentativas
                print("Novo Recorde Estabelecido \o/")
                
        elif(num < sorteio):
            print("O Numero Sorteado e MAIOR!\n")
            tentativas += 1
            
        else:
            print("O Numero Sortado e MENOR!\n")
            tentativas += 1
            
    jogar = int(input("\nDeseja jogar novamente? (1 - Sim / 2 - Nao): "))
    while(jogar != 1 and jogar != 2):
        print("Opcao Invalida!")
        jogar = int(input("\nDeseja jogar novamente? (1 - Sim / 2 - Nao): "))