from collections import Counter
import itertools
from api_lotofacil import capturar_ultimos_resultados

def ultimos_resultados(qtd=10):
    # Pega os últimos resultados via API (default 10 últimos)
    return capturar_ultimos_resultados(qtd)

def dezenas_mais_sorteadas(qtd=10):
    todas = [d for _, _, l in ultimos_resultados(qtd) for d in l]
    cont = Counter(todas)
    return cont.most_common(10)

def dezenas_menos_sorteadas(qtd=10):
    todas = [d for _, _, l in ultimos_resultados(qtd) for d in l]
    cont = Counter(todas)
    return cont.most_common()[-10:]

def trincas_mais_frequentes(qtd=10):
    todas_trincas = []
    for _, _, dezenas in ultimos_resultados(qtd):
        todas_trincas.extend(itertools.combinations(sorted(dezenas), 3))
    cont = Counter(todas_trincas)
    return cont.most_common(5)

def linhas_mais_frequentes(qtd=10):
    linhas = {1: range(1,6), 2: range(6,11), 3: range(11,16), 4: range(16,21), 5: range(21,26)}
    freq = Counter()
    for _, _, dezenas in ultimos_resultados(qtd):
        for l, nums in linhas.items():
            if any(d in nums for d in dezenas):
                freq[l] += 1
    return freq.most_common()

def colunas_mais_frequentes(qtd=10):
    colunas = {1: [1,6,11,16,21], 2: [2,7,12,17,22], 3: [3,8,13,18,23], 4: [4,9,14,19,24], 5: [5,10,15,20,25]}
    freq = Counter()
    for _, _, dezenas in ultimos_resultados(qtd):
        for c, nums in colunas.items():
            if any(d in nums for d in dezenas):
                freq[c] += 1
    return freq.most_common()

def faixas_mais_frequentes(qtd=10):
    faixas = {1: range(1,6), 2: range(6,11), 3: range(11,16), 4: range(16,21), 5: range(21,26)}
    freq = Counter()
    for _, _, dezenas in ultimos_resultados(qtd):
        for f, nums in faixas.items():
            if any(d in nums for d in dezenas):
                freq[f] += 1
    return freq.most_common()
