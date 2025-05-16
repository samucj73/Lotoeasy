import random

def gerar_cartoes(qtd):
    cartoes = []
    for _ in range(qtd):
        cartao = sorted(random.sample(range(1, 26), 15))
        cartoes.append(cartao)
    return cartoes