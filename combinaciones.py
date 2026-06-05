def fact_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def comb_calc(n, r):
    return fact_iter(n) // (fact_iter(r) * fact_iter(n - r))

def validate_bounds(n, r):
    if n < 0 or r < 0:
        return False
    if r > n:
        return False
    return True

def main():
    print("***COMBINATION CALCULATOR***")
    
    # Ingreso de datos directo sin try-except
    n = int(input("Enter n: "))
    r = int(input("Enter r: "))

    if not validate_bounds(n, r):
        print("Boundary error: It must satisfy 0 <= r <= n.")
        return

    # Calcular C(n, r) para la entrada válida
    print("\n1. CALCULATION")
    ans = comb_calc(n, r)
    print(f"C({n}, {r}) = {ans}")

    # Verificar automáticamente la identidad C(n, r) = C(n, n-r)
    print("\n2. IDENTITY VERIFICATION: C(n, r) == C(n, n-r)")
    ans_identity = comb_calc(n, n - r)
    print(f"C({n}, {r}) = {ans}")
    print(f"C({n}, {n}-{r}) -> C({n}, {n-r}) = {ans_identity}")
    
    if ans == ans_identity:
        print("-> Identity verified successfully.")
    else:
        print("-> Identity verification failed.")

    # Generar la fila n del triángulo de Pascal
    print(f"\n3. PASCAL'S TRIANGLE (ROW {n})")
    pascal_row = []
    for k in range(n + 1):
        pascal_row.append(comb_calc(n, k))
    print(f"Row {n}: {pascal_row}")

    # Imprimir ejemplos de uso
    print("\n4. USAGE EXAMPLES")
    c1 = comb_calc(5, 2)
    c2 = comb_calc(15, 4)
    print(f"Example A: Choosing 2 items from 5 -> C(5, 2) = {c1}")
    print(f"Example B: Choosing 4 items from 15 -> C(15, 4) = {c2}")

if __name__ == "__main__":
    main()