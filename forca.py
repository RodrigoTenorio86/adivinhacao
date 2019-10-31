
def jogar():

    print("******************************")
    print("Bem Vindo no Jogo forca")
    print("******************************")

    palavra_secreta = "banana"
    acertou = False
    enforcou = False
    index = 0
    while(not enforcou and not acertou):
        chute = input("Qual letra?  ")
        chute = chute.lower().strip()

        for letra in palavra_secreta:
            if(chute == letra):
                print("Encotrei a letra {} na posiçao {}".format(letra,index))
            index =index + 1


        print("Jogando...")


    print("fim")

if(__name__ == "__main__"):
    jogar()