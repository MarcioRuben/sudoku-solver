
'''vai returnar todos os numeros dos lugares preenchidos de um determinado quadrante'''
def numeros_ocupados_quadrante(x: int, y: int, table: list) -> list:
    ocupados = []
    if x < 3:
        if y < 3:
            for i in range(0, 3):
                for j in range(0, 3):
                    ocupados.append(table[i][j])
        elif y >= 3 and y < 6:
            for i in range(0, 3):
                for j in range(3, 6):
                    ocupados.append(table[i][j])
        elif y >= 6 and y < 9:
            for i in range(0, 3):
                for j in range(6, 9):
                    ocupados.append(table[i][j])
    elif x >= 3 and x < 6:
        if y < 3:
            for i in range(3, 6):
                for j in range(0, 3):
                    ocupados.append(table[i][j])
        elif y >= 3 and y < 6:
            for i in range(3, 6):
                for j in range(3, 6):
                    ocupados.append(table[i][j])
        elif y >= 6 and y < 9:
            for i in range(3, 6):
                for j in range(6, 9):
                    ocupados.append(table[i][j])
    elif x >= 6 and x < 9:
        if y < 3:
            for i in range(6, 9):
                for j in range(0, 3):
                    ocupados.append(table[i][j])
        elif y >= 3 and y < 6:
            for i in range(6, 9):
                for j in range(3, 6):
                    ocupados.append(table[i][j])
        elif y >= 6 and y < 9:
            for i in range(6, 9):
                for j in range(6, 9):
                    ocupados.append(table[i][j])
    return ocupados


'''vai returnar True caso um numero já exista na linha ou coluna do número selecionado'''
def is_in_line_column(table:list, x, y, value):
    #check line
    for i in range(9):
        if table[x][i] == value and i != y:
            return True
    
    #check row
    for j in range(9):
        if table[j][y] == value and j != x:
            return True
        
    return False


'''verifica se o número é único no quadrante'''
def number_in_box(quadrante: list, numero:int):
    counter = 0
    for i in range(9):
        if quadrante[i] == numero:
            counter += 1
    if counter == 1:
        return True
    else:
        return False



def print_table(table):
    for i in range(9):
        for j in range(9):
            if (j + 1) % 3 == 0 and j != 8:
                print(str(table[i][j])+'|', end="")
            else:
                print(table[i][j], end="")
        if (i + 1) % 3 == 0 and i != 8:
            print('\n')
            print('-'*11)
        print('\n')


'''retorna as coordenadas do espaço vazio'''
def find_empty(table: list):
    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
                return (i, j)
    return None


def solve_sudoku(table: list):
    #verifica se há espaços em branco(com 0)
    empty = find_empty(table)
    if not empty:
        return True
    else:
        linha, coluna = empty
        for value in range(1, 10):
            if is_in_line_column(table, linha, coluna, value) == False and (value not in numeros_ocupados_quadrante(linha, coluna, table)):
                table[linha][coluna] = value
                if solve_sudoku(table):
                    return True
                table[linha][coluna] = 0
    return False
                

unso = [[0, 0, 0, 2, 6, 0, 7, 0, 1], 
        [6, 8, 0, 0, 7, 0, 0, 9, 0], 
        [1, 9, 0, 0, 0, 4, 5, 0, 0], 
        [8, 2, 0, 1, 0, 0, 0, 4, 0], 
        [0, 0, 4, 6, 0, 2, 9, 0, 0], 
        [0, 5, 0, 0, 0, 3, 0, 2, 8], 
        [0, 0, 9, 3, 0, 0, 0, 7, 4], 
        [0, 4, 0, 0, 5, 0, 0, 3, 6], 
        [7, 0, 3, 0, 1, 8, 0, 0, 0]]


print_table(unso)
solve_sudoku(unso)
print('-'*11)
print_table(unso)

