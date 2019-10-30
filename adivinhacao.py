import random

print("******************************")
print("Bem Vindo no Jogo Adivinhacao")
print("******************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 3
rodada = 1

while( rodada <= total_de_tentativas ):
    print("Tentativa: {0} de {1}".format(rodada,total_de_tentativas))
   
    rodada = rodada + 1

    chute = input("Digite um numero entre 1 e 100: ")
    chute = int(chute)
    if(chute < 1 or chute > 100):
        print("numero Invalido.")
        continue

    print("Voce digitou", chute)

    acerto = chute == numero_secreto
    maior  = chute > numero_secreto
    menor  = chute < numero_secreto

    if(acerto):
        print("Acerto")
        break
    else:
        if(maior):
            print("Voce errou! O seu chute foi MAIOR.")
        elif(menor):
            print("Voce errou! O seu chute foi MENOR.")    

print("Numero secreto é  {}".format(numero_secreto) )
print("FIM.")