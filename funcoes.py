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