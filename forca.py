
import random



def jogar():
    
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta("palavras.txt")
    
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
            desenha_forca(erros)
           

        # enforcou = erros == 6

        # acertou = "_" not in letras_acertadas
        
        print(letras_acertadas) 
        
        if(erros == 7):
            enforcou = True
            break
        elif ("_" not in letras_acertadas):
            acertou = True
            break

           
    
    if(acertou):
        imprime_mensagem_vencedor()
        
    else:
        imprime_mensagem_perdedor(palavra_secreta)
       



def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

def carrega_palavra_secreta(nome_arquivo="palavras.txt", primeira_linha_valida=0):#Usando parametro opcional
    palavras = []

    # arquivo = open("palavras.txt", "r")

    # arquivo.close()

    with open(nome_arquivo) as arquivo: #Com a sintexe especial with ja se fechamento de arquivos automatico
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(primeira_linha_valida, len(palavras))
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
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()

