from collections import Counter
from itertools import combinations

# Concursos fictícios para análise (últimos 10)
concursos = [
    [1, 3, 5, 6, 8, 9, 10, 12, 13, 15, 16, 18, 20, 21, 25],
    [2, 4, 5, 6, 9, 11, 12, 14, 15, 17, 18, 20, 22, 24, 25],
    [1, 2, 5, 7, 9, 10, 11, 13, 14, 16, 17, 18, 21, 22, 23],
    [3, 5, 6, 8, 9, 10, 11, 13, 15, 17, 19, 20, 21, 23, 25],
    [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 18, 20, 22, 24],
    [2, 3, 5, 6, 9, 10, 12, 14, 15, 17, 19, 20, 22, 23, 25],
    [1, 4, 6, 7, 8, 10, 11, 13, 15, 16, 18, 19, 21, 23, 24],
    [2, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 18, 20, 21, 22],
    [3, 5, 7, 8, 10, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23],
    [1, 2, 3, 5, 6, 8, 10, 12, 13, 15, 17, 19, 20, 22, 25],
]

def dezenas_mais_sorteadas():
    todas = [num for concurso in concursos for num in concurso]
    contagem = Counter(todas)
    return contagem.most_common(10)

def dezenas_menos_sorteadas():
    todas = [num for concurso in concursos for num in concurso]
    contagem = Counter(todas)
    return contagem.most_common()[-10:]

def trincas_mais_sorteadas():
    trincas = []
    for concurso in concursos:
        trincas.extend(combinations(concurso, 3))
    contagem = Counter(trincas)
    return contagem.most_common(5)

def faixas_mais_sorteadas():
    faixas = [(1,5),(6,10),(11,15),(16,20),(21,25)]
    contagem = Counter()
    for concurso in concursos:
        for faixa in faixas:
            qtd = len([n for n in concurso if faixa[0] <= n <= faixa[1]])
            contagem[faixa] += qtd
    return contagem.most_common()

def linhas_mais_sorteadas():
    linhas = {i: [] for i in range(1, 6)}
    for concurso in concursos:
        for dezena in concurso:
            linha = (dezena - 1) // 5 + 1
            linhas[linha].append(dezena)
    return [(linha, len(linhas[linha])) for linha in linhas]

def colunas_mais_sorteadas():
    colunas = {i: [] for i in range(1, 6)}
    for concurso in concursos:
        for dezena in concurso:
            coluna = dezena % 5 if dezena % 5 != 0 else 5
            colunas[coluna].append(dezena)
    return [(coluna, len(colunas[coluna])) for coluna in colunas]