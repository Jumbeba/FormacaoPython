
import random

print('*********************************')
print('Bem vindo ao jogo de adivinhação!')
print('*********************************')

numero_secreto = random.randrange(0, 51)
total_de_tentativas = 3
rodada = 1

print(numero_secreto) # LINHA TEMPORÁRIA

for rodada in range(1, total_de_tentativas + 1):
    print(f"Tentativa {rodada} de {total_de_tentativas}")
    chute = int(input('Digite o seu número de 1 e 50: '))
    print('Você digitou', chute)

    if (chute < 1 or chute > 50):
        print("Você deve digitar um número entre 1 e 50!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto
    if acertou:
        print("Acertô mizeravi!!")
        break
    else:
        if maior:
            print("Você errou. SEU CHUTE FOI MAIOR que o número secreto.")
        elif menor:
            print("Você errou. SEU CHUTE FOI MENOR que o número secreto.")

print("Fim do jogo.")