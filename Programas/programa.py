from funcoes import preenche_frota
from funcoes import posicao_valida


tipos = ['porta-aviões', 'navio-tanque', 'contratorpedeiro', 'submarino']
frota = {
    'porta-aviões': [],
    'navio-tanque': [],
    'contratorpedeiro': [],
    'submarino': [],
}

for i in range(len(tipos)):
    tamanho = 4 - i
    quantidade = i + 1

    for j in range(quantidade):
        while True:
            print(f"Insira as informações referentes ao navio {tipos[i]} que possui tamanho {tamanho}")
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))

            if tamanho == 1:
                orientacao = 'vertical'
            else:
                orientacao_num = int(input('[1] Vertical [2] Horizontal: '))
                if orientacao_num == 1:
                    orientacao = 'vertical'
                else:
                    orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                preenche_frota(frota, tipos[i], linha, coluna, orientacao, tamanho)
                break
            else:
                print('Esta posição não está válida!')

print(frota)