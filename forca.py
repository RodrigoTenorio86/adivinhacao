
def jogar():

    print("******************************")
    print("Bem Vindo no Jogo forca")
    print("******************************")

    palavra_secreta = "banana"
    letras_acertadas= ["_", "_", "_", "_", "_", "_"]
    acertou = False
    enforcou = False

    while(not enforcou and not acertou):
        chute = input("Qual letra?  ")
        chute = chute.lower().strip()
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encotrei a letra {} na posiçao {}".format(letra,index))
                letras_acertadas[index] = letra
            index =index + 1

        print(letras_acertadas)
        print("Jogando...")


    print("fim")

if(__name__ == "__main__"):
    jogar()