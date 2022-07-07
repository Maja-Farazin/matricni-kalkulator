def vsota(mat1, mat2):
    vsota = []
    for i in range(len(mat1)):
        nova_vrsta = []
        for j in range(len(mat1[0])):
            nova_vrsta.append((mat1[i][j] + mat2[i][j]))
        vsota.append(nova_vrsta)
    return vsota

def razlika(mat1, mat2):
    razlika = []
    for i in range(len(mat1)):
        nova_vrsta = []
        for j in range(len(mat1[0])):
            nova_vrsta.append((mat1[i][j] - mat2[i][j]))
        razlika.append(nova_vrsta)
    return razlika

def mnozi_s_skalarjem(mat, skal):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = skal * mat[i][j]
    return mat


# Zmnožek dveh matrik
def zmnozek(mat1, mat2):
    zmnozek = []
    for i in range(len(mat1)):
        nova_vrsta = []
        for j in range(len(mat2[0])):
            element = 0
            for k in range(len(mat2)):
                element += (mat1[i][k] * mat2[k][j])
            nova_vrsta.append(element)
        zmnozek.append(nova_vrsta)
    return zmnozek


# Potenciranje matrike
def potenca(mat, stopnja):
    potencirana_mat = mat
    s = 1
    while s < stopnja:
        potencirana_mat = zmnozek(potencirana_mat, mat)
        s += 1
    return potencirana_mat

def sled(mat):
    sled = 0
    for i in range(len(mat)):
        sled += mat[i][i]
    return sled

def transponiraj(mat):
    transponiranka = [[0 for i in range(len(mat))] for j in range(len(mat[0]))]
    for j in range(len(mat)):
        for k in range(len(mat[0])):
            transponiranka[k][j] = mat[j][k]
    return transponiranka

# Vrne matriko brez a-te vrstica in b-tega stolpca
def podmatrika(mat, a, b):                       
    return [vrstica[:b - 1] + vrstica[b:] for vrstica in (mat[: a - 1] + mat[a:])]

def determinanta(mat):
    if len(mat) == 1:
        return mat[0][0]
    elif len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    else:                                        #razvoj po 1. vrstici
        det = 0
        for i in range(len(mat)):
            det += ((-1) ** i) * mat[0][i] * determinanta(podmatrika(mat, 1, i + 1))
        return det