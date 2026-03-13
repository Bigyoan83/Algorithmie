"""
TP 02 — Les Tableaux
Complétez les fonctions marquées TODO
"""


def rotate(arr: list, k: int) -> None:
    """
    Rotation circulaire droite de k positions, en place.
    Complexité attendue : O(n) temps, O(1) espace.
    Astuce : triple reverse.
    TODO
    """
    n = len(arr)
    if n == 0:
        return
    k = k % n  
 
    arr.reverse()           
    arr[:k] = arr[:k][::-1] 
    arr[k:] = arr[k:][::-1]

def remove_duplicates(arr: list) -> int:
    """
    Supprime les doublons d'un tableau TRIÉ en place.
    Retourne la nouvelle longueur.
    Complexité attendue : O(n).
    TODO
    """
    if not arr:
        return 0
 
    write = 1  
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:  
            arr[write] = arr[i]
            write += 1
    return write

def merge_arrays(a: list, b: list) -> list:
    """
    Fusionne deux tableaux triés en un seul tableau trié.
    Complexité attendue : O(n+m).
    TODO
    """
    result = []
    i, j = 0, 0
 
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
 
    result.extend(a[i:])  # ajoute ce qui reste de a
    result.extend(b[j:])  # ajoute ce qui reste de b
    return result


def binary_search(arr: list, target: int) -> int:
    """
    Recherche binaire dans un tableau trié.
    Retourne l'indice de target ou -1 si absent.
    Complexité attendue : O(log n).
    TODO
    """
    gauche, droite = 0, len(arr) - 1
 
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if arr[milieu] == target:
            return milieu
        elif arr[milieu] < target:
            gauche = milieu + 1  # on cherche à droite
        else:
            droite = milieu - 1  # on cherche à gauche
    return -1
 
def lower_bound(arr: list, target: int) -> int:

    """
    Premier indice i tel que arr[i] >= target.
    Retourne len(arr) si target > tous les éléments.
    Complexité attendue : O(log n).
    TODO
    """
    gauche, droite = 0, len(arr)
 
    while gauche < droite:
        milieu = (gauche + droite) // 2
        if arr[milieu] < target:
            gauche = milieu + 1
        else:
            droite = milieu
    return gauche


def upper_bound(arr: list, target: int) -> int:
    """
    Premier indice i tel que arr[i] > target.
    Retourne len(arr) si target >= tous les éléments.
    Complexité attendue : O(log n).
    TODO
    """
    gauche, droite = 0, len(arr)
 
    while gauche < droite:
        milieu = (gauche + droite) // 2
        if arr[milieu] <= target:
            gauche = milieu + 1
        else:
            droite = milieu
    return gauche


def transpose(m: list) -> None:
    """
    Transposée d'une matrice n×n en place.
    Complexité attendue : O(n²).
    TODO : échanger m[i][j] et m[j][i] pour j > i
    """
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]


def rotate_90(m: list) -> None:
    """
    Rotation 90° sens horaire en place.
    Étapes : transposer, puis inverser chaque ligne.
    TODO
    """
    transpose(m)
    for row in m:
        row.reverse()


def max_subarray(arr: list) -> int:
    """
    Sous-tableau contigu de somme maximale (algorithme de Kadane).
    Complexité attendue : O(n).
    TODO : cur = max(arr[i], cur + arr[i]) ; best = max(best, cur)
    """
    cur = best = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)  # on continue ou on recommence
        best = max(best, cur)  # on garde le meilleur
    return best
