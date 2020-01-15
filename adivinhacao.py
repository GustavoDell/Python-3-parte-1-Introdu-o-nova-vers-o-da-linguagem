import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_tentativa = int(3)
rodada = int(1)

print(numero_secreto)
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
        print("Você acertou")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que numero secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor que numero secreto.")

print("Fim do jogo")
