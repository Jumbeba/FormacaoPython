#importando os arquivos
import forca
import adivinhacao

#Função para escolher o jogo
def escolher_jogo():
    print('*********************************')
    print('********Escola o seu jogo!*******')
    print('*********************************')

    print('''O que você deseja jogar?
    [1] Forca
    [2] Adivinhação
    ''')
    jogo = int(input('Digite uma opção: '))

    if (jogo == 1):
        forca.jogar()
    elif (jogo == 2):
        adivinhacao.jogar()

#Condição para jogar diretamente do console ou terminal
if (__name__ == "__main__"):
    escolher_jogo()