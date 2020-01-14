print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentativa = int(3)
rodada = int(1)

while (rodada <= total_tentativa):
    print("Tentativa {} de {}".format(rodada, total_tentativa))
    chute_str  = input("Digite o seu numero: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    acerto = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acerto):
        print("Você acertou")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que numero secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor que numero secreto.")
    rodada = rodada + 1

print("Fim do jogo")
