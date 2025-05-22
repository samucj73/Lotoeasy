
import random
from collections import Counter

# Dezenas relevantes
PRIMOS = {2, 3, 5, 7, 11, 13, 17, 19, 23}
DEZENAS_POSSIVEIS = list(range(1, 26))

# Parâmetros considerados ideais com base em estatísticas
IDEAL_PARES = (6, 9)
IDEAL_SOMA = (170, 210)
IDEAL_PRIMOS = (4, 6)
IDEAL_SEQUENCIA_MAX = 3
IDEAL_QUADRANTES = (3, 4)

def contar_pares(cartao):
    return sum(1 for d in cartao if d % 2 == 0)

def contar_primos(cartao):
    return sum(1 for d in cartao if d in PRIMOS)

def calcular_soma(cartao):
    return sum(cartao)

def max_sequencia(cartao):
    seq = 1
    max_seq = 1
    for i in range(1, len(cartao)):
        if cartao[i] == cartao[i-1] + 1:
            seq += 1
            max_seq = max(max_seq, seq)
        else:
            seq = 1
    return max_seq

def contar_quadrantes(cartao):
    quadrantes = {
        1: set(range(1, 6)) | set(range(6, 11)),       # Quadrante 1 (1-10)
        2: set(range(11, 16)) | set(range(16, 21)),    # Quadrante 2 (11-20)
        3: set(range(21, 26))                         # Quadrante 3 (21-25)
    }
    usados = set()
    for d in cartao:
        for q, dezenas in quadrantes.items():
            if d in dezenas:
                usados.add(q)
    return len(usados)

def cartao_valido(cartao):
    pares = contar_pares(cartao)
    primos = contar_primos(cartao)
    soma = calcular_soma(cartao)
    seq = max_sequencia(cartao)
    quadrantes = contar_quadrantes(cartao)

    return (
        IDEAL_PARES[0] <= pares <= IDEAL_PARES[1] and
        IDEAL_PRIMOS[0] <= primos <= IDEAL_PRIMOS[1] and
        IDEAL_SOMA[0] <= soma <= IDEAL_SOMA[1] and
        seq <= IDEAL_SEQUENCIA_MAX and
        IDEAL_QUADRANTES[0] <= quadrantes <= IDEAL_QUADRANTES[1]
    )
    

def gerar_cartoes_personalizados( qtd_cartoes, fixas=None, excluir=None, mais_frequentes=None, atrasadas=None):
    qtd_cartoes
    fixas = fixas or []
    excluir = excluir or []
    mais_frequentes = set(mais_frequentes or [])
    atrasadas = set(atrasadas or [])

    dezenas_disponiveis = [d for d in DEZENAS_POSSIVEIS if d not in fixas and d not in excluir]
    
    if len(fixas) > 15:
        raise ValueError("Não é possível fixar mais de 15 dezenas.")
    if len(fixas) + len(dezenas_disponiveis) < 15:
        raise ValueError("Número insuficiente de dezenas disponíveis para gerar os cartões.")

    # Base ponderada pré-processada
    base_ponderada_original = []
    for d in dezenas_disponiveis:
        peso = 1
        if d in mais_frequentes:
            peso += 4
        if d in atrasadas:
            peso = max(peso - 1, 1)
        base_ponderada_original.extend([d] * peso)

    cartoes = set()
    tentativas = 0

    while len(cartoes) < qtd and tentativas < qtd * 1000:
        tentativas += 1
        cartao = set(fixas)

        base_ponderada = base_ponderada_original.copy()
        random.shuffle(base_ponderada)

        for dezena in base_ponderada:
            if len(cartao) >= 15:
                break
            cartao.add(dezena)

        if len(cartao) < 15:
            continue

        cartao_ordenado = tuple(sorted(cartao))
        if cartao_valido(cartao_ordenado):
            cartoes.add(cartao_ordenado)

    return [list(c) for c in cartoes]
