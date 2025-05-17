from collections import Counter

def validar_formato_jogos(jogos):
    if not isinstance(jogos, list):
        raise ValueError("Esperado uma lista de jogos.")
    for idx, item in enumerate(jogos):
        if not (isinstance(item, tuple) or isinstance(item, list)):
            raise ValueError(f"Item {idx} não é uma tupla/lista: {item}")
        if len(item) != 3:
            raise ValueError(f"Item {idx} não tem 3 elementos: {item}")
        _, _, dezenas = item
        if not (isinstance(dezenas, list) or isinstance(dezenas, tuple)):
            raise ValueError(f"Item {idx} o terceiro elemento não é lista/tupla: {dezenas}")
        for d in dezenas:
            if not isinstance(d, int):
                raise ValueError(f"Item {idx} dezenas contém valor não inteiro: {d}")
    print("Formato validado com sucesso!")

def pares_impares(jogos):
    resultado = Counter()
    for _, _, dezenas in jogos:
        pares = sum(1 for d in dezenas if d % 2 == 0)
        impares = 15 - pares
        resultado[(pares, impares)] += 1
    return resultado.items()

def soma_das_dezenas(jogos):
    faixas = Counter()
    for _, _, dezenas in jogos:
        soma = sum(dezenas)
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
    for _, _, dezenas in jogos:
        for q, nums in quadrante_map.items():
            count = len(set(dezenas) & nums)
            resultado[q] += count
    return resultado.items()

def sequencias_comuns(jogos):
    contador = Counter()
    for _, _, dezenas in jogos:
        seq = []
        for i in range(len(dezenas)):
            if i == 0 or dezenas[i] == dezenas[i-1] + 1:
                seq.append(dezenas[i])
            else:
                if len(seq) >= 3:
                    contador[tuple(seq)] += 1
                seq = [dezenas[i]]
        if len(seq) >= 3:
            contador[tuple(seq)] += 1
    return contador.most_common(5)

def duplas_mais_comuns(jogos):
    contador = Counter()
    for _, _, dezenas in jogos:
        for i in range(len(dezenas)):
            for j in range(i+1, len(dezenas)):
                dupla = tuple(sorted((dezenas[i], dezenas[j])))
                contador[dupla] += 1
    return contador.most_common(5)

def repeticoes_com_concursos(jogos):
    contador = Counter()
    for i in range(1, len(jogos)):
        anterior = set(jogos[i-1][2])
        atual = set(jogos[i][2])
        repetidas = len(anterior & atual)
        contador[repetidas] += 1
    return sorted(contador.items())

def dezenas_atrasadas(jogos):
    todas = set(range(1, 26))
    recentes = set(num for _, _, dezenas in jogos for num in dezenas)
    return sorted(todas - recentes)

def quantidade_primos(jogos):
    primos = {2, 3, 5, 7, 11, 13, 17, 19, 23}
    contador = Counter()
    for _, _, dezenas in jogos:
        qtd = sum(1 for d in dezenas if d in primos)
        contador[qtd] += 1
    return sorted(contador.items(), key=lambda x: -x[1])
