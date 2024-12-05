A = [[1, 2], [3, 4]]  
B = [[5, 6], [7, 8]]

A2 = [[1, 2, 3], [4, 5, 6]]  
B2 = [[7, 8], [9, 10], [11, 12]]

Z = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Z2 = [[2, 3, 4], [1, 2]]



# Scrivi una funzione che prenda in input due matrici della stessa dimensione 
# e restituisca una nuova matrice che rappresenta la loro somma.
def sumMatrix(A, B):
    assert len(A) == len(B), "Devono avere la stessa dimensione"
    assert len(A[0]) == len(B[0]), "Devono avere la stessa dimensione"
    
    return [[col_A + col_B for col_A, col_B in zip(row_A, row_B)] for row_A, row_B in zip(A, B)]



#Soluzione senza agire sui dati ma sugli indici:
def sumMatrixIndex(A, B):
    assert len(A) == len(B), "Devono avere la stessa dimensione"
    assert len(A[0]) == len(B[0]), "Devono avere la stessa dimensione"
    
    return [[A[row][col] + B[row][col] for col in range(len(A[row]))] for row in range(len(A))]



#Funzione che calcola il prodotto tra matrici
def prodMatrix(A, B):
    assert len(A[0]) == len(B), "Dimensione non appropriata" 
    
    matrix = [[0] * len(B[0]) for _ in range(len(A))]
    
    for row in range(len(A)):
        for col in range(len(B[row])):
            for i in range(len(B)):
                matrix[row][col] += A[row][i] * B[i][col]
                
    return matrix



#Trovare la diagonale della matrice
def diagonale(matrix):
    diagonale = list()
    
    i = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if col == i:
                diagonale.append(matrix[row][col])
        i += 1
    
    return diagonale



#Funzione per moltiplicare una matrice per uno scalare (valida anche per dimensioni diverse)
def prodscalmatrix(matrix, scalare=1):
    return [[matrix[row][col] * scalare for col in range(len(matrix[row]))]
            for row in range(len(matrix))]



#Funzione che somma gli elementi sopra la diagonale principale
def sumDiagMatrix(matrix):
    i = somma = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if col > i:
                somma += matrix[row][col]
        i += 1
    
    return somma



#Funzione che unisce 2 matrici (Verticalmente, righe)
def matrixUnionOrizz(matrixA, matrixB):
    return matrixA + matrixB




#Funzione che unisce 2 matrici (Orizzontalmente, colonne)
def matrixUnionVertical(matrixA, matrixB):
    assert len(matrixA) == len(matrixB), "Devono avere lo stesso numero di righe"
    
    return [row_A + row_B for row_A, row_B in zip(matrixA, matrixB)]



#Ordinare in base al totale più alto degli elementi di ogni riga
def orderBasingOnTotal(matrix):
    return sorted(matrix, key = sum, reverse = True)



print(sumMatrix(A, B))
print(sumMatrixIndex(A, B))
print(prodMatrix(A2, B2))
print(diagonale(Z))
print(prodscalmatrix(Z2, 3))
print(sumDiagMatrix(Z))
print(matrixUnionOrizz(A, B))
print(matrixUnionVertical(A, B))
print(orderBasingOnTotal(Z))