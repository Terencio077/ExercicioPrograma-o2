def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])
        elif orientacao == 'horizontal':
            posicoes.append([linha, coluna + i])
    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes_navio = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = []
    frota[nome_navio].append(posicoes_navio)
    return frota
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
def posiciona_frota(frota):
    grid = [[0 for _ in range(10)] for _ in range(10)]
    for navio in frota.values():
        for posicoes in navio:
            for linha, coluna in posicoes:
                grid[linha][coluna] = 1
    return grid
def afundados(frota, tabuleiro):
    contador = 0
    for navios in frota.values():
        for posicoes in navios:
            afundado = True
            for linha, coluna in posicoes:
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
            if afundado:
                contador += 1
    return contador
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])
        elif orientacao == 'horizontal':
            posicoes.append([linha, coluna + i])
    return posicoes

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for l, c in posicoes:
        if not (0 <= l < 10 and 0 <= c < 10):
            return False
    ocupadas = set()
    for navios in frota.values():
        for p in navios:
            for l, c in p:
                ocupadas.add((l, c))
    for l, c in posicoes:
        if (l, c) in ocupadas:
            return False
    return True

