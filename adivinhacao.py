import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativa = int(0)
    rodada = int(1)
    pontos = int(1000)
    perdeu = False

    print("Qual nivel de dificuldade?")

    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_tentativa = 20
    elif(nivel == 2):
        total_tentativa = 10
    else:
        total_tentativa = 5
        

    for rodada in range(1, total_tentativa + 1):
        
        print("Tentativa {} de {}".format(rodada, total_tentativa))
        chute_str  = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100!")
            continue

        acerto = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acerto):
            perdeu = False
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            perdeu = True
            if(maior):
                print("Você errou! O seu chute foi maior que numero secreto.")

            elif(menor):
                print("Você errou! O seu chute foi menor que numero secreto.")
            
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            
    if(perdeu):
        print("Sua pontuação foi de {}, e numero secreto era {}".format(pontos, numero_secreto))

    print("Fim do jogo")

