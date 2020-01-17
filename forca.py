
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not acertou and not enforcou):

        chute = input("Qual letra?")
        chute = chute.strip().upper() #strip() é uma função do python que remove espaços das variveis
        
        if(chute in palavra_secreta):
            index = 0
        
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Voce possui {} tentativas".format(6-erros))

        # enforcou = erros == 6

        # acertou = "_" not in letras_acertadas
        
        print(letras_acertadas) 
        
        if(erros == 6 or "_" not in letras_acertadas):
            enforcou = True
            acertou = True
            break

           
    
    if(acertou):
        print("Você ganhou")
    else:
        print("Você perdeu")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()