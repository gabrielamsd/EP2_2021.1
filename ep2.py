# implementando o número de cartas de um baralho completo e embaralhando elas
import random
def cria_baralho():
    baralho = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠','A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']
    random.shuffle(baralho)
    return baralho

# extrai o naipe de uma carta quando a função recebe essa carta
def extrai_naipe(string):
    naipe = string[-1]
    return naipe

# extrai o valor de uma carta quando a função recebe essa carta
def extrai_valor(string):
    if string[1] == '0':
        valor = string[0:2]
        return valor
    else:
        valor = string[0]
        return valor

# vendo as possíveis posições de uma carta dentro de uma lista de cartas durante o jogo   
def lista_movimentos_possiveis(baralho, i):
    if i == 0:
        return []
    if i>0 and i<3:
        if (extrai_valor(baralho[i]) == extrai_valor(baralho[i-1])) or (extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-1])):
            return [1] 
        else:
            return []
    if i >= 3:
        mesmo_valor_1 = (extrai_valor(baralho[i]) == extrai_valor(baralho[i-1]))
        mesmo_valor_3 = (extrai_valor(baralho[i]) == extrai_valor(baralho[i-3]))
        mesmo_naipe_1 = (extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-1]))
        mesmo_naipe_3 = (extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-3]))

        if (mesmo_valor_1 or mesmo_naipe_1 ) and ( mesmo_valor_3 or mesmo_naipe_3 ):
            return [1, 3]
        elif mesmo_valor_1 or mesmo_naipe_1:
            return [1]
        elif mesmo_valor_3 or mesmo_naipe_3:
            return [3]
        
        else:
            return []


baralho = ['6♥', 'J♥', '9♣', '9♥']
print(baralho)
print(lista_movimentos_possiveis(baralho, 3))

# empilha a carta sendo observada nao lugar da carta de destino escolhida (sempre 1 ou 3 para trás da posição da inicial da carta)
def empilha(baralho, inicial, final):
    baralho[final] = baralho[inicial]
    del baralho[inicial]
    return baralho
    
# verifica se ainda existem movimentos a ser feitos nesse baralho
def possui_movimentos_possiveis(baralho):
    for e in range(len(baralho)):
        if lista_movimentos_possiveis(baralho, e) == [1] or lista_movimentos_possiveis(baralho, e) == [3] or lista_movimentos_possiveis(baralho, e) == [1, 3]:
            return True
    return False


baralho_do_jogador = cria_baralho()
inválido = True
while inválido:
    print(' O jogo funciona da seguinte forma; Seu objetivo é empilhar todas as cartas do baraho. As únicas regras para emplihá-las são: \n A carta que você colocar por cima da outra deve conter ou o mesmo naipe ou o mesmo valor que ela. \n A carta que você vai mover deve sempre estar imediatamente ou tres cartas depois da carta de destino.')
    começar_jogo = input('Digite "C" para começar a jogar: ')
    if começar_jogo != 'C':
        print('Entrada Inválida')

    else:
        inválido = False
            print(baralho_do_jogador)

            inicial = int(input('Qual é a posição da carta que você quer mexer? Comece a contar do 0! \n posição inicial: '))
            possibilidades = lista_movimentos_possiveis(baralho_do_jogador, inicial)
            final = int(input('Qual é a posição para a qual você quer mover essa carta? \n posição final: '))
            if inicial - final == 1 or inicial - final == 3:            
                if lista_movimentos_possiveis(baralho_do_jogador, inicial) == []:
                    print('Você não pode fazer esse movimento, tente novamene: ')
                if (lista_movimentos_possiveis(baralho_do_jogador, inicial) == [1] and inicial - final == 1) or (lista_movimentos_possiveis(baralho_do_jogador, inicial) == [3] and inicial - final == 3) or (lista_movimentos_possiveis(baralho_do_jogador, inicial) == [1, 3] and (inicial - final == 1) or (inicial - final ==3)):         
                    baralho_do_jogador = empilha(baralho_do_jogador, inicial, final)
                    print('Ok, próxima rodada: ')
                else:
                    print('Você não pode fazer esse movimento, tente novamentee: ')
                if possui_movimentos_possiveis(baralho_do_jogador) == False:
                    if len(baralho_do_jogador) > 1:
                        print('Você não possui mais movimentos possíveis... Você perdeu :( ')
                    if len(baralho_do_jogador) = 1:
                        print('Parabéms! Você ganhou o jogo :) ')
            else:
                print('Você não pode fazer esse movimento, tente novamente: ')
