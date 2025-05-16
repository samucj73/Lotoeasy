from collections import Counter

def pares_impares(jogos):
    resultado = Counter()
    for jogo in jogos:
        pares = sum(1 for d in jogo if d % 2 == 0)
        impares = 15 - pares
        resultado[(pares, impares)] += 1
    return resultado.items()

def soma_das_dezenas(jogos):
    faixas = Counter()
    for jogo in jogos:
        soma = sum(jogo)
        faixa = (soma // 10) * 10
        faixas[faixa] += 1
    return faixas.items()

def quadrantes(jogos):
    quadrante_map = {
        1: set(range(1, 6)),
        2: set(range(6, 11)),
        3: set(range(11, 16)),
        4: set(range(16, 21)),
        5: set(range(21, 26))
    }
    resultado = Counter()
    for jogo in jogos:
        for q, nums in quadrante_map.items():
            count = len(set(jogo) & nums)
            resultado[q] += count
    return resultado.items()

def sequencias_comuns(jogos):
    contador = Counter()
    for jogo in jogos:
        seq = []
        for i in range(len(jogo)):
            if i == 0 or jogo[i] == jogo[i-1] + 1:
                seq.append(jogo[i])
            else:
                if len(seq) >= 3:
                    contador[tuple(seq)] += 1
                seq = [jogo[i]]
        if len(seq) >= 3:
            contador[tuple(seq)] += 1
    return contador.most_common(5)

def duplas_mais_comuns(jogos):
    contador = Counter()
    for jogo in jogos:
        for i in range(len(jogo)):
            for j in range(i+1, len(jogo)):
                dupla = tuple(sorted((jogo[i], jogo[j])))
                contador[dupla] += 1
    return contador.most_common(5)

def repeticoes_com_concursos(jogos):
    contador = Counter()
    for i in range(1, len(jogos)):
        anterior = set(jogos[i-1])
        atual = set(jogos[i])
        repetidas = len(anterior & atual)
        contador[repetidas] += 1
    return sorted(contador.items())

def dezenas_atrasadas(jogos):
    todas = set(range(1, 26))
    recentes = set(num for jogo in jogos for num in jogo)
    return sorted(todas - recentes)

def quantidade_primos(jogos):
    primos = {2, 3, 5, 7, 11, 13, 17, 19, 23}
    contador = Counter()
    for jogo in jogos:
        qtd = sum(1 for d in jogo if d in primos)
        contador[qtd] += 1
    return sorted(contador.items(), key=lambda x: -x[1])
