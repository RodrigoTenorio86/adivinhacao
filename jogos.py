import adivinhacao
import forca

def escolhe_jogo():
    print("(1) Forca (2) Adivinhacao")

    jogo = int(input("Escolha o jogo: "))

    if(jogo == 1):
        forca.jogar()
    elif(jogo==2):
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()