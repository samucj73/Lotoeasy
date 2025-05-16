import random
from lotofacil_estatisticas import ultimos_resultados

def gerar_cartoes_personalizados(fixas, excluir, quantidade):
    ultimos = [n for _, dezenas in ultimos_resultados() for n in dezenas]
    base = list(set(ultimos))
    base = [d for d in base if d not in fixas and d not in excluir]
    cartoes = []

    for _ in range(quantidade):
        complemento = random.sample(base, 15 - len(fixas))
        cartao = sorted(set(fixas + complemento))
        while len(cartao) < 15:
            novo = random.choice([n for n in range(1, 26) if n not in cartao and n not in excluir])
            cartao.append(novo)
        cartoes.append(sorted(cartao))

    return cartoes
