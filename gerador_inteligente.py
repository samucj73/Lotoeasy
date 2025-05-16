import random
from collections import Counter

# Configurações com base nas estatísticas analisadas
PRIMOS = {2, 3, 5, 7, 11, 13, 17, 19, 23}
DEZENAS_POSSIVEIS = list(range(1, 26))

# Parâmetros ideais com base nos últimos resultados analisados
IDEAL_PARES = (6, 9)           # entre 6 e 9 pares
IDEAL_SOMA = (170, 210)        # soma entre 170 e 210
IDEAL_PRIMOS = (4, 6)          # entre 4 e 6 primos
IDEAL_REPETIDAS = (7, 10)      # entre 7 e 10 repetidas do concurso anterior (opcional)

def contar_pares(cartao):
    return sum(1 for d in cartao if d % 2 == 0)

def contar_primos(cartao):
    return sum(1 for d in cartao if d in PRIMOS)

def calcular_soma(cartao):
    return sum(cartao)

def gerar_cartoes_inteligentes(qtd, fixas=None, excluir=None, mais_frequentes=None, atrasadas=None):
    fixas = fixas or []
    excluir = excluir or []
    mais_frequentes = set(mais_frequentes or [])
    atrasadas = set(atrasadas or [])
    cartoes = set()

    tentativas = 0
    while len(cartoes) < qtd and tentativas < qtd * 500:
        tentativas += 1

        # Começa com as dezenas fixas
        cartao = set(fixas)

        # Base: dezenas possíveis, excluindo fixas e excluídas
        base_dezenas = [d for d in DEZENAS_POSSIVEIS if d not in fixas and d not in excluir]

        # Prioriza dezenas mais frequentes e evita as atrasadas
        base_ponderada = []
        for d in base_dezenas:
            peso = 1
            if d in mais_frequentes:
                peso += 2
            if d in atrasadas:
                peso -= 1
            base_ponderada.extend([d] * max(peso, 1))

        random.shuffle(base_ponderada)

        while len(cartao) < 15 and base_ponderada:
            cartao.add(base_ponderada.pop())

        cartao = sorted(cartao)

        # Critérios de aceitação
        pares = contar_pares(cartao)
        primos = contar_primos(cartao)
        soma = calcular_soma(cartao)

        if IDEAL_PARES[0] <= pares <= IDEAL_PARES[1] and \
           IDEAL_PRIMOS[0] <= primos <= IDEAL_PRIMOS[1] and \
           IDEAL_SOMA[0] <= soma <= IDEAL_SOMA[1]:
            cartoes.add(tuple(cartao))

    return [sorted(list(c)) for c in cartoes]
