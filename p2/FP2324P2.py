# This is the Python script for your project


# Class intersecao
class intersecao:
    

    # Inicializa a classe
    def __init__(self, col, row):
        # Caso a variavel coluna nao seja uma string e a variavel row nao seja um inteiro
        if type(col) != str or type(row) != int:
            raise ValueError("cria_intersecao: argumentos invalidos")

        # Caso as variaveis col e row nao estejam dentro dos parametros permitidos
        if len(col) != 1 or row < 1 or row > 19 or col < "A" or col > "S":
            raise ValueError("cria_intersecao: argumentos invalidos")

        self.col = col
        self.row = row

    # Funcao que permite comparar uma intersecao a outra
    def __eq__(self, other):
        return self.col == other.col and self.row == other.row

    # Funcao que permite utilizar a funcao hash na classe intersecao
    def __hash__(self):
        return hash(self.col)


###
#    Construtores
###


# Da return a uma nova intersecao
def cria_intersecao(col, row):
    return intersecao(col, row)


###
#    Seletores
###


# Da return a variavel col da intersecao
def obtem_col(arg):
    return arg.col


##Da return a variavel row da intersecao
def obtem_lin(arg):
    return arg.row


###
#    Reconhecedores
###


# Verifica se o tipo de uma variavel e intersecao
def eh_intersecao(arg):
    return type(arg) == intersecao


###
#    Testes
###


# Verifica se 2 intersecoes sao iguais
def intersecoes_iguais(i1, i2):
    if not eh_intersecao(i1) or not eh_intersecao(i2):
        return False

    return i1 == i2


###
#    Transformadores
###


# Passa uma intersecao para uma variavel do tipo string
def intersecao_para_str(i):
    return obtem_col(i) + str(obtem_lin(i))


# Passa uma string para uma variavel do tipo intersecao
def str_para_intersecao(i):
    return cria_intersecao(i[0], int(i[1:]))


###
#    Funções de alto nível
###


# Obtem as intersecoes adjacentes a intersecao passada como argumento
def obtem_intersecoes_adjacentes(i, l):
    result = ()
    row = obtem_lin(i)
    col = obtem_col(i)

    if row != 1:
        aux = cria_intersecao(col, row - 1)
        result += (aux,)

    if col != "A":
        aux = cria_intersecao(chr(ord(col) - 1), row)
        result += (aux,)

    if col != obtem_col(l):
        aux = cria_intersecao(chr(ord(col) + 1), row)
        result += (aux,)

    if row != obtem_lin(l):
        aux = cria_intersecao(col, row + 1)
        result += (aux,)

    return result


# Retorna um tuplo com as intersecoes ordenadas
def ordena_intersecoes(tup):
    return tuple(sorted(tup, key=lambda a: (obtem_lin(a), obtem_col(a))))


# Class pedra
class pedra:
    
    # Inicializa uma variavel do tipo pedra
    def __init__(self, cor):
        if cor not in ["O", "X", "."]:
            raise ValueError("cria_pedra: argumento invalido")
        self.cor = cor

    # Compara duas variaveis do tipo pedra
    def __eq__(self, other):
        return self.cor == other.cor


###
#    Construtores
###


# Cria uma pedra branca, ou seja, cuja cor e igual a "O"
def cria_pedra_branca():
    return pedra("O")


# Cria uma pedra preta, ou seja, cuja cor e igual a "X"
def cria_pedra_preta():
    return pedra("X")


# Cria uma pedra neutra, ou seja, cuja cor e igual a "."
def cria_pedra_neutra():
    return pedra(".")


###
#    Reconhecedores
###


# Verifica se o argumento e uma variavel do tipo pedra
def eh_pedra(arg):
    return type(arg) == pedra


# Verifica se o argumento e uma pedra branca
def eh_pedra_branca(arg):
    if not eh_pedra(arg):
        return False

    return arg.cor == "O"


# Verifica se o argumento e uma pedra preta
def eh_pedra_preta(arg):
    if not eh_pedra(arg):
        return False

    return arg.cor == "X"


# Verifica se o argumento e uma pedra neutra
def eh_pedra_neutra(arg):
    if not eh_pedra(arg):
        return False

    return arg.cor == "."


###
#    Testes
###


# Verifica se 2 pedras sao iguais
def pedras_iguais(p1, p2):
    if not eh_pedra(p1) or not eh_pedra(p2):
        return False

    return p1 == p2


###
#    Transformadores
###


# Transforma uma variavel do tipo pedra em uma variavel do tipo str
def pedra_para_str(p):
    return p.cor


###
#    Funções de alto nível
###


# Verifica se o argumento e uma pedra branca ou preta
def eh_pedra_jogador(p):
    return p.cor != "."


# Class goban
class goban:
   

    #Inicializa uma variavel do tipo goban
    def __init__(self, tamanho, intersecoes_brancas, intersecoes_pretas, flag):
        if type(tamanho) != int:
            if flag == 0:
                raise ValueError("cria_goban_vazio: argumento invalido")
            else:
                raise ValueError("cria_goban: argumentos invalidos")

        if tamanho not in [9, 13, 19]:
            if flag == 0:
                raise ValueError("cria_goban_vazio: argumento invalido")
            else:
                raise ValueError("cria_goban: argumentos invalidos")

        self.tamanho = tamanho

        self.tabuleiro = [
            [cria_pedra_neutra() for i in range(tamanho)] for j in range(tamanho)
        ]

        visited = [[False for i in range(tamanho)] for j in range(tamanho)]

        if type(intersecoes_brancas) != tuple or type(intersecoes_pretas) != tuple:
            raise ValueError("cria_goban: argumentos invalidos")

        if intersecoes_brancas != ():
            for i in intersecoes_brancas:
                if not eh_intersecao(i):
                    raise ValueError("cria_goban: argumentos invalidos")

                col = ord(obtem_col(i)) - 65
                row = obtem_lin(i) - 1

                if col > tamanho - 1 or row > tamanho - 1:
                    raise ValueError("cria_goban: argumentos invalidos")

                if visited[row][col] == True:
                    raise ValueError("cria_goban: argumentos invalidos")

                visited[row][col] = True
                self.tabuleiro[row][col] = cria_pedra_branca()

        if intersecoes_pretas != ():
            for i in intersecoes_pretas:
                if not eh_intersecao(i):
                    raise ValueError("cria_goban: argumentos invalidos")

                col = ord(obtem_col(i)) - 65
                row = obtem_lin(i) - 1

                if col > tamanho - 1 or row > tamanho - 1:
                    raise ValueError("cria_goban: argumentos invalidos")

                if visited[row][col] == True:
                    raise ValueError("cria_goban: argumentos invalidos")

                visited[row][col] = True
                self.tabuleiro[row][col] = cria_pedra_preta()

    #Permite comparar duas variaveis do tipo goban
    def __eq__(self, other):
        return self.tabuleiro == other.tabuleiro  # and g1.tamanho == g2.tamanho


###
#    Construtores
###

#Cria um novo goban cujo tabuleiro so contem pedras neutras
def cria_goban_vazio(tamanho):
    return goban(tamanho, (), (), 0)

#Cria um novo goban cujo as intersecoes presentes no tuplo ib contem
#pedras brancas e as presentes no tuplo ip contem pedras pretas
def cria_goban(tamanho, ib, ip):
    return goban(tamanho, ib, ip, 1)

#Cria um novo goban copia do argumento
def cria_copia_goban(g):
    ib = ()
    ip = ()

    for row in range(g.tamanho):
        for col in range(g.tamanho):
            if eh_pedra_branca(g.tabuleiro[row][col]):
                inter = cria_intersecao(chr(col + 65), row + 1)
                ib += (inter,)

            if eh_pedra_preta(g.tabuleiro[row][col]):
                inter = cria_intersecao(chr(col + 65), row + 1)
                ip += (inter,)

    return cria_goban(g.tamanho, ib, ip)


###
#    Seletores
###

#Obtem o canto superior direito de um goban como intersecao
def obtem_ultima_intersecao(t):
    tamanho = t.tamanho
    return intersecao(chr(tamanho + 64), tamanho)

#Obtem a pedra presente na intersecao i do goban g
def obtem_pedra(g, i):
    col = ord(obtem_col(i)) - 65
    row = obtem_lin(i) - 1

    return g.tabuleiro[row][col]

#Obtem todas as intersecoes conectadas cuja variavel cor 
#da pedra seja igual
def obtem_cadeia(g, i):
    p = obtem_pedra(g, i)

    result = (i,)

    col = ord(obtem_col(i)) - 65
    row = obtem_lin(i) - 1

    size = g.tamanho

    visited = [[False for i in range(size)] for j in range(size)]
    visited[row][col] = True

    canto = obtem_ultima_intersecao(g)

    queue = []
    queue.append(i)

    while queue:
        new_intersecao = queue.pop(0)
        aux = obtem_intersecoes_adjacentes(new_intersecao, canto)

        for j in aux:
            col = ord(obtem_col(j)) - 65
            row = obtem_lin(j) - 1

            if visited[row][col] == False and pedras_iguais(g.tabuleiro[row][col], p):
                result += (j,)
                queue.append(j)

            visited[row][col] = True

    return ordena_intersecoes(result)


###
#    Modificadores
###

#Coloca uma variavel do tipo pedra na intersecao i do goban g
def coloca_pedra(g, i, p):
    col = ord(obtem_col(i)) - 65
    row = obtem_lin(i) - 1

    g.tabuleiro[row][col] = p

    return g

#Remove uma variavel do tipo pedra na intersecao i do goban g
def remove_pedra(g, i):
    col = ord(obtem_col(i)) - 65
    row = obtem_lin(i) - 1

    g.tabuleiro[row][col] = cria_pedra_neutra()

    return g

#Transforma todas as intersecoes presentes no tuplo t
# em pedras neutras
def remove_cadeia(g, t):
    for i in t:
        g = remove_pedra(g, i)

    return g


###
#    Reconhecedores
###

#Verifica se o argumento e um goban
def eh_goban(g):
    return type(g) == goban

#Verifica se a intersecao i faz parte do goban g
def eh_intersecao_valida(g, i):
    col = ord(obtem_col(i)) - 65
    row = obtem_lin(i) - 1
    tamanho = g.tamanho

    if col < 0 or row < 0 or row > tamanho - 1 or col > tamanho - 1:
        return False

    return True


###
#    Testes
###

#Verifica se 2 gobans sao iguais
def gobans_iguais(g1, g2):
    if not eh_goban(g1) or not eh_goban(g2):
        return False

    return g1 == g2


###
#    Transformadores
###

#Transforma uma variavel do tipo goban em uma variavel do tipo str
def goban_para_str(g):
    result = "  "

    for i in range(g.tamanho):
        # Escreve as letras
        result += " " + chr(i + 65)
    result += "\n"

    # Escreve o valor da intersecao.
    for i in range(g.tamanho):
        if g.tamanho - i < 10:
            result += " "
        result += str(g.tamanho - i)
        for j in range(g.tamanho):
            result += " " + pedra_para_str(g.tabuleiro[g.tamanho - i - 1][j])

        if g.tamanho - i < 10:
            result += " "
        result += " " + str(g.tamanho - i) + "\n"

    result += "  "
    # Escreve as letras novamente
    for i in range(g.tamanho):
        result += " " + chr(i + 65)
    return result


###
#    Funções de alto nível
###

#Da return a um tuplo cujo conteudo e os territorios do goban g
def obtem_territorios(g):
    result = ()
    aux = ()
    visited = [[False for i in range(g.tamanho)] for j in range(g.tamanho)]

    for i in range(g.tamanho):
        for j in range(g.tamanho):
            if eh_pedra_neutra(g.tabuleiro[i][j]) and visited[i][j] == False:
                aux = obtem_cadeia(g, cria_intersecao(chr(j + 65), i + 1))

                for w in aux:
                    row = obtem_lin(w) - 1
                    col = ord(obtem_col(w)) - 65
                    visited[row][col] = True

                result += (aux,)

    return result

#Obtem as intersecoes adjacentes cujas pedras tem valor diferentes das
#do tuplo dado como argumento
def obtem_adjacentes_diferentes(g, t):
    row = obtem_lin(t[0]) - 1
    col = ord(obtem_col(t[0])) - 65

    result = ()

    canto = obtem_ultima_intersecao(g)

    visited = [[False for i in range(g.tamanho)] for j in range(g.tamanho)]

    if eh_pedra_neutra(g.tabuleiro[row][col]):
        for inter in t:
            aux = obtem_intersecoes_adjacentes(inter, canto)

            for adj in aux:
                row = obtem_lin(adj) - 1
                col = ord(obtem_col(adj)) - 65

                if visited[row][col] == False and eh_pedra_jogador(
                    g.tabuleiro[row][col]
                ):
                    visited[row][col] = True
                    result += (adj,)

    else:
        for inter in t:
            aux = obtem_intersecoes_adjacentes(inter, canto)

            for adj in aux:
                row = obtem_lin(adj) - 1
                col = ord(obtem_col(adj)) - 65

                if visited[row][col] == False and eh_pedra_neutra(
                    g.tabuleiro[row][col]
                ):
                    visited[row][col] = True
                    result += (adj,)

    return ordena_intersecoes(result)

#Efetua uma jogada, ou seja, coloca uma pedra p na intersecao i do goban g
def jogada(g, i, p):
    g = coloca_pedra(g, i, p)
    canto = obtem_ultima_intersecao(g)

    adj = obtem_intersecoes_adjacentes(i, canto)

    for inter in adj:
        row = obtem_lin(inter) - 1
        col = ord(obtem_col(inter)) - 65

        if eh_pedra_jogador(g.tabuleiro[row][col]) and not pedras_iguais(
            g.tabuleiro[row][col], p
        ):
            aux = obtem_cadeia(g, inter)

            if obtem_adjacentes_diferentes(g, aux) == ():
                g = remove_cadeia(g, aux)

    return g

#Da return ao numero de pedras no goban de cada jogador
def obtem_pedras_jogadores(g):
    brancas = 0
    pretas = 0
    for i in range(g.tamanho):
        for j in range(g.tamanho):
            if eh_pedra_branca(g.tabuleiro[i][j]):
                brancas += 1
            else:
                if eh_pedra_preta(g.tabuleiro[i][j]):
                    pretas += 1

    result = (brancas, pretas)

    return result


###
#    Funções adicionais
###

#Calcula os pontos de ambos os jogadores
def calcula_pontos(g):
    pedras = obtem_pedras_jogadores(g)

    brancas = pedras[0]
    pretas = pedras[1]

    if pretas == 0 and brancas != 0:
        return (g.tamanho * g.tamanho, 0)

    if brancas == 0 and pretas != 0:
        return (0, g.tamanho * g.tamanho)

    if brancas == 0 and pretas == 0:
        return (0, 0)

    territorios = obtem_territorios(g)

    for territorio in territorios:
        row = obtem_lin(territorio[0]) - 1
        col = ord(obtem_col(territorio[0])) - 65

        if not eh_pedra_jogador(g.tabuleiro[row][col]):
            adjacentes = obtem_adjacentes_diferentes(g, territorio)
            p = 0
            b = 0

            for adjacente in adjacentes:
                row2 = obtem_lin(adjacente) - 1
                col2 = ord(obtem_col(adjacente)) - 65

                if eh_pedra_branca(g.tabuleiro[row2][col2]):
                    b = 1
                else:
                    p = 1

            if p == 1 and not b == 1:
                pretas += len(territorio)

            if b == 1 and not p == 1:
                brancas += len(territorio)

    return (brancas, pretas)

#Define se uma jogada e legal no jogo go
def eh_jogada_legal(g, i, p, l):
    copia = cria_copia_goban(g)

    if not eh_intersecao_valida(g, i):
        return False

    row = obtem_lin(i) - 1
    col = ord(obtem_col(i)) - 65

    if eh_pedra_jogador(copia.tabuleiro[row][col]):
        return False

    copia = jogada(copia, i, p)

    aux = obtem_cadeia(copia, i)

    if obtem_adjacentes_diferentes(copia, aux) == ():
        return False

    if gobans_iguais(copia, l):
        return False

    return True

#Funcao que le a jogada de um jogador de go
def turno_jogador(g, p, l):
    while 1:
        if eh_pedra_branca(p):
            inter = input("Escreva uma intersecao ou 'P' para passar [O]:")
        else:
            inter = input("Escreva uma intersecao ou 'P' para passar [X]:")

        if inter == "P":
            return False

        if type(inter) != int:
            if 1 < len(inter) < 4:
                i = str_para_intersecao(inter)

                if eh_jogada_legal(g, i, p, l):
                    g = jogada(g, i, p)
                    return True

#Funcao que permite inicializar e jogar continuamente o jogo go
def go(n, tb, tp):
    if type(n) != int:
        raise ValueError("go: argumentos invalidos")

    if n not in [9, 13, 19] or type(tb) != tuple or type(tp) != tuple:
        raise ValueError("go: argumentos invalidos")

    fim = 0

    if tb != ():
        for x in tb:
            if not 1 < len(x) < 4:
                raise ValueError("go: argumentos invalidos")

            if type(x[0]) != str or not "1" < x[1:] < str(n):
                raise ValueError("go: argumentos invalidos")

            if x[0] < "A" or x[0] > chr(n + 64):
                raise ValueError("go: argumentos invalidos")

    if tp != ():
        for x in tp:
            if not 1 < len(x) < 4:
                raise ValueError("go: argumentos invalidos")

            if type(x[0]) != str or not "1" < x[1:] < str(n):
                raise ValueError("go: argumentos invalidos")

            if x[0] < "A" or x[0] > chr(n + 64):
                raise ValueError("go: argumentos invalidos")

    tb = tuple(str_para_intersecao(x) for x in tb)
    tp = tuple(str_para_intersecao(x) for x in tp)

    g = cria_goban(n, tb, tp)
    jogada = 0

    while 1:
        pontos = calcula_pontos(g)
        print("Branco (O) tem", pontos[0], "pontos")
        print("Preto (X) tem", pontos[1], "pontos")
        print(goban_para_str(g))

        if jogada % 2 == 0:
            p = cria_pedra_preta()
        else:
            p = cria_pedra_branca()

        jogada += 1

        l = cria_copia_goban(g)

        if turno_jogador(g, p, l):
            fim = 0
        else:
            fim += 1

        if fim == 2:
            print("Branco (O) tem", pontos[0], "pontos")
            print("Preto (X) tem", pontos[1], "pontos")
            print(goban_para_str(g))
            break

    pontos = calcula_pontos(g)

    return pontos[0] > pontos[1]
