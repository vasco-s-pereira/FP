def eh_territorio(grid):
    #Verifica se a grid e um tuplo vazio ou tem apenas 1 numero
    if grid == () or isinstance(grid, int) == True:
        return False

    #Verifica se a grid esta vazia
    if len(grid) == 0:
        return False

    #Verifica se a grid e um tuplo
    if isinstance(grid, tuple) == False:
        return False

    #Guarda o numero de linhas da primeira coluna
    if isinstance(grid[0], int) == True:
        length = 1
    else:
        length = len(grid[0])

    #Caso o numero de colunas seja superior a 26 ou as linhas sejam superiores a 99
    if length > 99 or len(grid) > 26:
        return False

    for tuplos in grid:
        #Verifica se os valores das linhas estao guardados em tuplos
        if isinstance(tuplos, tuple) == False:
            return False
        #Verifica se a length e igual a length da 1 coluna
        if isinstance(tuplos, int) == True:
            if length != 1:
                return False
        else:
            if len(tuplos) != length:
                return False
        #Verifica se os valores dentro dos tuplos sao inteiros cujo valor e 1 ou 0
        for valor in tuplos:
            if isinstance(valor, int) == False or (valor != 0 and valor != 1):
                return False

    return True


def obtem_ultima_intersecao(grid):
    #Obtem a letra correspondente a ultima coluna da grid
    letter = chr(64 + len(grid))
    #Cria o tuplo result cujo primeiro elemento e a letra e o segundo e o numero de linhas
    result = (letter, len(grid[0]))
    return result


def eh_intersecao(intersecao):
    #Verifica se o tuplo esta vazio ou tem apenas um inteiro
    if isinstance(intersecao, int) == True or intersecao == ():
        return False

    #Verifica se e um tuplo
    if isinstance(intersecao, tuple) == False:
        return False

    #Verifica se o primeiro e um tuplo
    if isinstance(intersecao[0], tuple) == True:
        return False

    #Verifica que a length e igual a 2
    if len(intersecao) != 2:
        return False

    #Verifica se os elementos sao uma string e um int respetivamente
    if (
        isinstance(intersecao[0], str) == True
        and isinstance(intersecao[1], int) == True
    ):
        letra = intersecao[0]
        numero = intersecao[1]
    else:
        return False

    #Verifica se o primeiro elemento e so uma letra
    if len(letra) != 1:
        return False

    #Verifica se os elementos estao entre os limites dados
    if letra > "Z" or letra < "A" or numero > 99 or numero < 1:
        return False

    return True


def eh_intersecao_valida(grid, intersecao):
    #Verifica se a intersecao existe segundo os limites definidos
    if eh_intersecao(intersecao) == False:
        return False
    #Verifica se a intersecao pode existir na grid dada
    if len(grid) < ord(intersecao[0]) - 64 or len(grid[0]) < intersecao[1]:
        return False
    return True


def eh_intersecao_livre(grid, intersecao):
    #Verifica se a intersecao existe na grid dada
    if eh_intersecao_valida(grid, intersecao) == False:
        return False
    coluna = ord(intersecao[0]) - 65
    linha = intersecao[1] - 1

    #Verifica se o valor da intersecao na grid e igual a 0 (Livre)
    return grid[coluna][linha] == 0


def obtem_intersecoes_adjacentes(grid, intersecao):
    result = ()
    aux = ()
    letra = intersecao[0]
    numero = intersecao[1]

    #Obtem as intersecoes adjacentes a intersecao dada respeitando os limites da grid
    if numero != 1:
        aux = (letra, numero - 1)
        result += (aux,)

    if letra != "A":
        aux = (chr(ord(letra) - 1), numero)
        result += (aux,)
    if ord(letra) - 64 < len(grid):
        aux = (chr(ord(letra) + 1), numero)
        result += (aux,)

    if numero != len(grid[0]):
        aux = (letra, numero + 1)
        result += (aux,)

    return result


def ordena_intersecoes(tup):
    #Ordena o tuplo atraves da funcao sort
    #Utiliza o segundo elemento como primeira comparacao
    #Utiliza a funcao tuple para transformar o resutado num tuplo
    return tuple(sorted(tup, key=lambda a: (a[1], a[0])))


def territorio_para_str(grid):
    #Verifica se a grid e um territorio
    if eh_territorio(grid) == False:
        raise ValueError("territorio_para_str: argumento invalido")

    #Espacos iniciais
    result = "  "
    for i in range(len(grid)):
        #Escreve as letras
        result += " " + chr(i + 65)
    result += "\n"
    #Escreve o valor da intersecao. ( X se for 1 e . se for 0)
    for i in range(len(grid[0])):
        if len(grid[0]) - i < 10:
            result += " "
        result += str(len(grid[0]) - i)
        for j in range(len(grid)):
            if grid[j][len(grid[0]) - 1 - i] == 0:
                result += " ."
            else:
                result += " X"
        if len(grid[0]) - i < 10:
            result += " "
        result += " " + str(len(grid[0]) - i) + "\n"

    result += "  "
    #Escreve as letras novamente
    for i in range(len(grid)):
        result += " " + chr(i + 65)
    return result


def obtem_cadeia(grid, intersecao):
    #Verificacoes iniciais da grid e da intersecao
    if (
        eh_intersecao(intersecao) == False
        or eh_intersecao_valida(grid, intersecao) == False
        or eh_territorio(grid) == False
    ):
        raise ValueError("obtem_cadeia: argumentos invalidos")

    #Algoritmo BFS que utiliza a funcao obtem_intersecoes_adjacentes para obter as intersecoes adjacentes a inicial
    #Utiliza a variavel queue como estrutura de dados FIFO
    #Utiliza a variavel visited para guardar quais intersecoes ja foram visitadas de forma a evitar repeticoes no resultado final
    result = (intersecao,)

    letra = ord(intersecao[0]) - 65
    numero = intersecao[1] - 1

    value = grid[letra][numero]

    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    visited[letra][numero] = True

    queue = []
    queue.append(intersecao)

    while queue:
        new_intersecao = queue.pop(0)
        aux = obtem_intersecoes_adjacentes(grid, new_intersecao)

        for i in range(len(aux)):
            letra = ord(aux[i][0]) - 65
            numero = aux[i][1] - 1

            if visited[letra][numero] == False and grid[letra][numero] == value:
                result += (aux[i],)
                queue.append(aux[i])

            visited[letra][numero] = True

    return ordena_intersecoes(result)


def obtem_vale(grid, intersecao):

    #Novamente algoritmo BFS com pequenas modificacoes no codigo de forma a obter os vales e nao as cadeias
    letra = ord(intersecao[0]) - 65
    numero = intersecao[1] - 1
    result = ()

    if (
        eh_intersecao_valida(grid, intersecao) == False
        or eh_territorio(grid) == False
        or grid[letra][numero] != 1
    ):
        raise ValueError("obtem_vale: argumentos invalidos")

    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    visited[letra][numero] = True

    queue = []
    queue.append(intersecao)

    while queue:
        new_intersecao = queue.pop(0)
        aux = obtem_intersecoes_adjacentes(grid, new_intersecao)

        for i in range(len(aux)):
            letra = ord(aux[i][0]) - 65
            numero = aux[i][1] - 1
            if visited[letra][numero] == False:
                visited[letra][numero] = True
                if grid[letra][numero] == 1:
                    queue.append(aux[i])
                else:
                    result += (aux[i],)

    return ordena_intersecoes(result)


def verifica_conexao(grid, inter1, inter2):
    #Verifica se tanto a grid como as intersecoes sao validas
    if (
        eh_intersecao_valida(grid, inter1) == False
        or eh_territorio(grid) == False
        or eh_intersecao_valida(grid, inter2) == False
        or eh_intersecao(inter1) == False
        or eh_intersecao(inter2) == False
    ):
        raise ValueError("verifica_conexao: argumentos invalidos")
    #Obtem a cadeia de ambas as intersecoes
    cadeia1 = obtem_cadeia(grid, inter1)
    cadeia2 = obtem_cadeia(grid, inter2)

    #Caso facam parte da mesma cadeia retorna true
    return cadeia1 == cadeia2


def calcula_numero_montanhas(grid):
    if eh_territorio(grid) == False:
        raise ValueError("calcula_numero_montanhas: argumento invalido")

    count = 0

    #Percorre a grid inteira e adiciona 1 por cada montanha que encontrar (intersecao com valor 1)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += 1

    return count


def calcula_numero_cadeias_montanhas(grid):
    if eh_territorio(grid) == False:
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")

    count = 0

    existe = 0
    intersecao = ()
    aux = ()

    #Variavel lista guarda todas as cadeias do territorio
    lista = []

    #Percorre a grid toda e obtem a cadeia caso o valor da intersecao seja 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                existe = 0
                intersecao = (chr(i + 65), j + 1)
                aux = obtem_cadeia(grid, intersecao)
                #Verifica se a cadeia ja existe na lista
                for w in range(count):
                    if lista[w] == aux:
                        existe = 1
                #Caso nao exista adiciona a cadeia a lista e adiciona 1 a count
                if existe == 0:
                    lista.append(aux)
                    count += 1

    return count


def calcula_tamanho_vales(grid):
    if eh_territorio(grid) == False:
        raise ValueError("calcula_tamanho_vales: argumento invalido")

    lista = []
    existe = 0
    intersecao = ()

    #Percorre a grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                intersecao = (chr(i + 65), j + 1)
                #Obtem o vale de todas as intersecoes que tenham valor 1
                aux = obtem_vale(grid, intersecao)
                
                #Caso o vale nao existe na variavel lista este e adicionado
                for vale in aux:
                    existe = 0
                    for counter in lista:
                        if vale == counter:
                            existe = 1
                    if existe == 0:
                        lista.append(vale)

    #Da return ao tamanho da lista que tem todos os vales guardados
    return len(lista)

