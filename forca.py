def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo da forca!***')
    print('*********************************')

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    # Enquanto (True)
    while (not enforcou and not acertou):

        chute = input("Qual letra? ").strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                    letras_faltando = str(letras_acertadas.count('_'))
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)
        print(f'Ainda faltam {letras_faltando} letras.')

    if(acertou):
        print('Você ganhou!!!!')
    else:
        print('Você perdeu. :( ')

    print('Fim do jogo')

if (__name__ == "__main__"):
    jogar()

