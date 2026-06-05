def fact_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def perm_calc(n, r):
    return fact_iter(n) // fact_iter(n - r)

def validate_bounds(n, r):
    if n < 0 or r < 0:
        return False
    if r > n:
        return False
    return True

def main():
    print("***PERMUTATION CALCULATOR***")
    
    try:
        n = int(input("Enter n: "))
        r = int(input("Enter r: "))
    except ValueError:
        print("Input error: Please enter valid integers.")
        return

    if not validate_bounds(n, r):
        print("Boundary error: It must satisfy 0 <= r <= n.")
        return

    # Mostrar procedimiento y calcular n! y P(n,r)
    print("\nPROCEDURE")
    n_fact = fact_iter(n)
    minus_fact = fact_iter(n - r)
    ans = perm_calc(n, r)
    
    print(f"1. Calculate n! -> {n}! = {n_fact}")
    print(f"2. Calculate (n-r)! -> ({n}-{r})! = {n - r}! = {minus_fact}")
    print(f"3. Apply formula -> P({n},{r}) = {n_fact} / {minus_fact} = {ans}")

    # Comparar al menos dos casos requeridos
    print("\nCASE COMPARISONS")
    p1 = perm_calc(10, 3)
    p2 = perm_calc(20, 5)
    print(f"Case A: P(10, 3) = {p1}")
    print(f"Case B: P(20, 5) = {p2}")
    if p2 > p1:
        print(f"Comparison: Case B is larger than Case A by a factor of {p2 // p1}x.")

if __name__ == "__main__":
    main()