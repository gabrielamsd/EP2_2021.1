from funcoes import *

baralho_do_jogador = cria_baralho()
inválido = True
while inválido:
    
    print(' O jogo funciona da seguinte forma; Seu objetivo é empilhar todas as cartas do baraho. As únicas regras para emplihá-las são: \n A carta que você colocar por cima da outra deve conter ou o mesmo naipe ou o mesmo valor que ela. \n A carta que você vai mover deve sempre estar imediatamente ou tres cartas depois da carta de destino.')
    começar_jogo = input('Digite "enter" para começar a jogar: ')
    if começar_jogo != '':
        print('Entrada Inválida')

    else:
        jogando = True
        inválido = False
        while jogando:

            print(cartas(baralho_do_jogador))

            inicial = int(input('Qual é a posição da carta que você quer mexer? \nposição inicial: '))
            possibilidades = lista_movimentos_possiveis(baralho_do_jogador, inicial)
            final = int(input('Qual é a posição para a qual você quer mover essa carta? \nposição final: '))
            #inicial += 1
            #final += 1
            if inicial - final == 1 or inicial - final == 3:            
                if lista_movimentos_possiveis(baralho_do_jogador, inicial) == []:
                    print('Você não pode fazer esse movimento, tente novamente: ')
                elif (lista_movimentos_possiveis(baralho_do_jogador, inicial) == [1] and inicial - final == 1) or (lista_movimentos_possiveis(baralho_do_jogador, inicial) == [3] and inicial - final == 3) or (lista_movimentos_possiveis(baralho_do_jogador, inicial) == [1, 3] and (inicial - final == 1) or (inicial - final ==3)):         
                    baralho_do_jogador = empilha(baralho_do_jogador, inicial, final)
                    print('Ok, próxima rodada: ')

                else:
                    print('Você não pode fazer esse movimento, tente novamente: ')
                if possui_movimentos_possiveis(baralho_do_jogador) == False:
                    if len(baralho_do_jogador) > 1:
                        print('Você não possui mais movimentos possíveis... Você perdeu :( ')
                        jogando == False
                        
                    if len(baralho_do_jogador) == 1:
                        print('Parabéns! Você ganhou o jogo :) ')
                        jogando == False
                        
            else:
                print('Você não pode fazer esse movimento, tente novamente: ')