
import random



def jogar():
    
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not acertou and not enforcou):

        chute = pede_chute()
        
        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Voce possui {} tentativas".format(6-erros))

        # enforcou = erros == 6

        # acertou = "_" not in letras_acertadas
        
        print(letras_acertadas) 
        
        if(erros == 6):
            enforcou = True
            break
        elif ("_" not in letras_acertadas):
            acertou = True
            break

           
    
    if(acertou):
        print("Você ganhou")
    else:
        print("Você perdeu")
    print("Fim do jogo")


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    palavras = []

    # arquivo = open("palavras.txt", "r")

    # arquivo.close()

    with open("palavras.txt") as arquivo: #Com a sintexe especial with ja se fechamento de arquivos automatico
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    
    return ["_" for letra in palavra]#List Comprehensions

def pede_chute():

    chute = input("Qual letra?")
    chute = chute.strip().upper() #strip() é uma função do python que remove caracteres especiais
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1

if(__name__ == "__main__"):
    jogar()