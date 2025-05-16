from collections import Counter
import itertools

def ultimos_resultados():
    return [
        (3094, [2, 3, 5, 6, 7, 9, 10, 11, 14, 16, 17, 20, 21, 23, 25]),
        (3093, [1, 3, 4, 5, 6, 7, 10, 12, 13, 14, 17, 18, 22, 24, 25]),
        (3092, [1, 2, 4, 6, 8, 9, 10, 11, 12, 14, 15, 16, 20, 22, 25]),
        (3091, [3, 5, 6, 7, 8, 10, 11, 12, 14, 16, 18, 19, 21, 23, 24]),
        (3090, [2, 3, 4, 5, 7, 9, 10, 13, 15, 16, 18, 20, 21, 24, 25]),
        (3089, [1, 2, 3, 5, 6, 8, 10, 12, 14, 15, 17, 18, 20, 23, 25]),
        (3088, [1, 4, 5, 6, 7, 9, 11, 12, 13, 14, 16, 18, 19, 22, 24]),
        (3087, [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 15, 17, 20, 24]),
        (3086, [2, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18, 22, 24]),
        (3085, [1, 2, 3, 4, 6, 8, 10, 12, 14, 16, 17, 19, 20, 22, 23]),
    ]

def dezenas_mais_sorteadas():
    todas = [d for _, l in ultimos_resultados() for d in l]
    cont = Counter(todas)
    return cont.most_common(10)

def dezenas_menos_sorteadas():
    todas = [d for _, l in ultimos_resultados() for d in l]
    cont = Counter(todas)
    return cont.most_common()[-10:]

def trincas_mais_frequentes():
    todas_trincas = []
    for _, dezenas in ultimos_resultados():
        todas_trincas.extend(itertools.combinations(sorted(dezenas), 3))
    cont = Counter(todas_trincas)
    return cont.most_common(5)

def linhas_mais_frequentes():
    linhas = {1: range(1,6), 2: range(6,11), 3: range(11,16), 4: range(16,21), 5: range(21,26)}
    freq = Counter()
    for _, dezenas in ultimos_resultados():
        for l, nums in linhas.items():
            if any(d in nums for d in dezenas):
                freq[l] += 1
    return freq.most_common()

def colunas_mais_frequentes():
    colunas = {1: [1,6,11,16,21], 2: [2,7,12,17,22], 3: [3,8,13,18,23], 4: [4,9,14,19,24], 5: [5,10,15,20,25]}
    freq = Counter()
    for _, dezenas in ultimos_resultados():
        for c, nums in colunas.items():
            if any(d in nums for d in dezenas):
                freq[c] += 1
    return freq.most_common()

def faixas_mais_frequentes():
    faixas = {1: range(1,6), 2: range(6,11), 3: range(11,16), 4: range(16,21), 5: range(21,26)}
    freq = Counter()
    for _, dezenas in ultimos_resultados():
        for f, nums in faixas.items():
            if any(d in nums for d in dezenas):
                freq[f] += 1
    return freq.most_common()
