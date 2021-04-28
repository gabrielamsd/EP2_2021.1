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

        if ((extrai_valor(baralho[i]) == extrai_valor(baralho[i-1])) or (extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-1]))) and ((extrai_valor(baralho[i]) == extrai_valor(baralho[i-3])) or (extrai_naipe(baralho[i])== extrai_naipe(baralho[i-3]))):
            return [1, 3]
        elif (extrai_valor(baralho[i]) == extrai_valor(baralho[i-1])) or (extrai_naipe(baralho[i]) == extrai_naipe(baralho[i-1])):
            return [1]
        elif (extrai_valor(baralho[i]) == extrai_valor(baralho[i-3])) or (extrai_naipe(baralho[i])== extrai_naipe(baralho[i-3])):
            return [3]
        
        else:
            return []

# empilha a carta sendo observada nao lugar da carta de destino escolhida (sempre 1 ou 3 para trás da posição da inicial da carta)
def empilha(baralho, inicial, final):
    baralho[final] = baralho[inicial]
    del baralho[inicial]
    return baralho