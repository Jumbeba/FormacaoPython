#Regra de pontuação do jogo: A diferença entre o seu chute e o númeo secreto será DESCONTADO dos seus pontos

import random

def jogar():
    print('*********************************')
    print('Bem vindo ao jogo de adivinhação!')
    print('*********************************')

    numero_secreto = random.randrange(0, 51)
    total_de_tentativas = 0
    pontos = 1000

    print('''
    Qual o nível de dificuldade que você deseja?
    [1] Fácil
    [2] Médio
    [3] Difícil''')

    nivel = int(input('Defina o seu nível: '))
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute = int(input('Digite o seu número de 1 e 50: '))
        print('Você digitou', chute)

        # Tratamento de erro do usuário
        if (chute < 1 or chute > 50):
            print("Você deve digitar um número entre 1 e 50!")
            continue

        #Lógica
        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if acertou:
            print("Acertô mizeravi!!")
            print(f'Você fez {pontos} pontos. Parabéns!')
            break
        else:
            if maior:
                print("Você errou. Seu chute foi MAIOR que o número secreto.\n")
            elif menor:
                print("Você errou. Seu chute foi MENOR que o número secreto.\n")
            # Contagem de pontos
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print("Fim do jogo.")

if (__name__ == "__main__"):
    jogar()
