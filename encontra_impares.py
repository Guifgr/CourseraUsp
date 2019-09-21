def encontra_impares (n):
    if not n:
        return []
    if n % 2 == 1:
        return [n[0]] + encontra_impares(n[1:]) 
    return encontra_impares(n[1:])