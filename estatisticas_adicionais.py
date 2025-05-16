
from collections import Counter
from itertools import combinations

def pares_impares(resultados):
    contador = Counter()
    for dezenas in resultados:
        pares = len([d for d in dezenas if d % 2 == 0])
        impares = 15 - pares
        contador[(pares, impares)] += 1
    return sorted(contador.items(), key=lambda x: x[1], reverse=True)

def soma_das_dezenas(resultados):
    faixas = Counter()
    for dezenas in resultados:
        soma = sum(dezenas)
        faixa = (soma // 10) * 10  # Arredonda para faixa de 10
        faixas[faixa] += 1
    return sorted(faixas.items(), key=lambda x: x[0])

def quadrantes(resultados):
    # Quadrantes: 1 (1-5,6-10), 2 (11-15,16-20), 3 (21-25)
    def identificar_quadrante(n):
        if n <= 10:
            return 1
        elif n <= 20:
            return 2
        else:
            return 3
    contagem = Counter()
    for dezenas in resultados:
        quadrantes = [identificar_quadrante(d) for d in dezenas]
        for q in set(quadrantes):
            contagem[q] += 1
    return sorted(contagem.items())

def sequencias_comuns(resultados):
    contagem = Counter()
    for dezenas in resultados:
        sorted_d = sorted(dezenas)
        seq = []
        for i in range(len(sorted_d) - 1):
            if sorted_d[i] + 1 == sorted_d[i + 1]:
                if not seq:
                    seq = [sorted_d[i], sorted_d[i + 1]]
                else:
                    seq.append(sorted_d[i + 1])
            else:
                if len(seq) >= 3:
                    contagem[tuple(seq)] += 1
                seq = []
        if len(seq) >= 3:
            contagem[tuple(seq)] += 1
    return contagem.most_common(5)

def duplas_mais_comuns(resultados):
    contagem = Counter()
    for dezenas in resultados:
        for dupla in combinations(sorted(dezenas), 2):
            contagem[dupla] += 1
    return contagem.most_common(5)

def repeticoes_com_concursos(resultados):
    repeticoes = Counter()
    for i in range(1, len(resultados)):
        atual = set(resultados[i])
        anterior = set(resultados[i - 1])
        repetidas = len(atual & anterior)
        repeticoes[repetidas] += 1
    return sorted(repeticoes.items())

def dezenas_atrasadas(resultados, total_dezenas=25):
    ultimas = set()
    for dezenas in resultados[:10]:
        ultimas.update(dezenas)
    atrasadas = [d for d in range(1, total_dezenas + 1) if d not in ultimas]
    return sorted(atrasadas)
