"""
TP 01 — Analyse de Complexité & Benchmarks
Complétez les sections marquées TODO
"""
import time
import random


# ── Exercice 1 ────────────────────────────────────────────────────────────────

def func_a(n: int) -> int:
    """
    Complexité : O(n²)
    Il y a 2 boucles imbriqués (i de 0 à n-1, et j de i à n-1).
    Le nombres total d'opérations et de : n(n+1)/2
    """
    s = 0
    for i in range(n):
        for j in range(i, n):
            s += 1
    return s


def func_b(n: int) -> int:
    """
    Complexité : 0(log n)
    i double à chaque tour (i *=2)
    Le nombre d'itérations = llog₂(n) -> O(log n).
    """
    c, i = 0, 1
    while i < n:
        c += 1
        i *= 2
    return c


# ── Exercice 2 ────────────────────────────────────────────────────────────────

def find_pair_naive(arr: list, target: int) -> bool:
    """
    Retourne True si deux éléments distincts de arr somment à target.
    Complexité attendue : O(n²)
    TODO: deux boucles imbriquées
    """
    for i in range(len(arr)):
        for j in range (i+ 1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False


def find_pair_fast(arr: list, target: int) -> bool:
    """
    Retourne True si deux éléments distincts de arr somment à target.
    Complexité attendue : O(n)
    TODO: une passe avec un set — pour chaque x, chercher (target-x)
    """
    seen = set()
    for x in arr:
        complement = target - x 
        if complement in seen:
            return True
        seen.add(x)
    return False


# ── Exercice 3 ────────────────────────────────────────────────────────────────

def run_benchmark():
    """Mesure et affiche les temps d'exécution des deux versions."""
    print(f"{'n':>8}  {'naïf (ms)':>12}  {'rapide (ms)':>12}")
    print("-" * 40)
    for n in [1_000, 5_000, 10_000, 50_000]:
        arr = random.sample(range(n * 10), n)
        target = arr[0] + arr[n // 2]

        # TODO: mesurez find_pair_naive avec time.perf_counter()
        start = time.perf_counter()
        find_pair_naive(arr, target)
        t_naive = time.perf_counter() - start

        # TODO: mesurez find_pair_fast
        start = time.perf_counter()
        find_pair_fast(arr, target)
        t_fast = time.perf_counter() -start

        print(f"{n:>8}  {t_naive * 1000:>12.3f}  {t_fast * 1000:>12.3f}")


if __name__ == "__main__":
    run_benchmark()
