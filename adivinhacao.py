print("******************************")
print("Bem Vindo no Jogo Adivinhacao")
print("******************************")

numero_secreto = 42

chute = input("Digite o seu numero: ")
chute = int(chute)
print("Voce digitou", chute)

acerto = chute == numero_secreto
maior  = chute > numero_secreto
menor  = chute < numero_secreto
if(acerto):
    print("Acerto")
else:
    if(maior):
        print("Voce errou! O seu chute foi MAIOR.")
    elif(menor):
        print("Voce errou! O seu chute foi MENOR.")    

print("FIM.")