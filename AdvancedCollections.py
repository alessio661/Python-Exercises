A = [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]

M = [[2, 3, 4],
     [5, 6, 7],
     [8, 9, 10]]

T = [(0, 1), (1, 2), (2, 0)]



#Funzione per ruotare una matrice di 90, 180, 270 e 360 gradi in senso orario
def rotateMatrix(matrix, grade=90):
    if grade == 90:
        return [[row[i] for row in matrix][::-1] for i in range(len(matrix[0]))]
    elif grade == 180:
        return [row[::-1] for row in matrix[::-1]]
    elif grade == 270:
        return [[row[i] for row in matrix] for i in range(len(matrix[0]))][::-1]
    elif grade == 360:
        return matrix
    


#Funzione che per ogni riga e colonna indicata dalla tupla, moltiplica i loro prodotti
def MatrixXTuple(matrix, tupla):
    out = []

    for riga, colonna in tupla:
        ris_riga = ris_colonna = 1
        
        for elemento in matrix[riga]:
            ris_riga *= elemento
            
        for i in range(len(matrix)):
            ris_colonna *= matrix[i][colonna]
            
        out.append(ris_riga * ris_colonna)
    return out



MATRICE = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 1],
           [2, 3, 5, 7, 4],
           [7, 8, 9, 2, 5],
           [6, 9, 1, 4, 2]]



#Funzione che trova le diagonali oblique, il punto centrale
#e le coordinate del punto centrale e le diagonali orizzontali e verticali che partono da esso
#La funzione ritorna una nuova matrice che visualizza unicamente le diagonali che sono state trovate
#(Per semplicità la matrice in ogni riga non ha elementi uguali)
def diagonals(matrix):
    diag_sx = [row[i] for row in matrix for i in range(len(matrix[len(row) - 1])) if i == matrix.index(row)]
    diag_dx = [row[i] for row in matrix[::-1] for i in range(len(matrix[len(row) - 1])) if i == matrix[::-1].index(row)]
    
    assert len(matrix) % 2 == 1, "La matrice non è di dimensioni dispare, non vi è il centro"
    
    center_coords = (int((len(matrix) - 1) / 2), int((len(matrix) - 1) / 2))
    center = matrix[center_coords[0]][center_coords[1]]
    
    diag_orizz = matrix[center_coords[0]]
    diag_vertic = [row[i] for row in matrix for i in range(len(matrix[len(row) - 1])) if i == center_coords[1]]
    
    ###Creazione nuova matrice
    empty = [[None] * len(matrix[0]) for _ in range(len(matrix))]
    
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == diag_sx[row]:
                empty[row][col] = diag_sx[row]
            
            if matrix[::-1][row][col] == diag_dx[row]:
                empty[::-1][row][col] = diag_dx[row]
                
            if row == center_coords[0]:
                empty[row][col] = diag_orizz[col]
            
            if matrix[row][col] == diag_vertic[row]:
                empty[row][col] = diag_vertic[row]
     
    for row in empty:
        print(row)
    
    return center

            
print(rotateMatrix(A), " 90 gradi")
print(rotateMatrix(A, 180), " 180 gradi")
print(rotateMatrix(A, 270), " 270 gradi")
print(rotateMatrix(A, 360), " 360 gradi")

print(MatrixXTuple(M, T))

print(diagonals(MATRICE))




            
        
    