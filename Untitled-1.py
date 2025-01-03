#2,3,5,7...
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def primes_linear(n):
    if n <= 1:
        raise ValueError("O número deve ser maior que 1.")
    return [i for i in range(2, n + 1) if is_prime(i)]

def primes_recursive(n, current=2, primes_list=None):
    if primes_list is None:
        primes_list = []

    if n <= 1:
        raise ValueError("O número deve ser maior que 1.")

    if current > n:
        return primes_list

    if is_prime(current):
        primes_list.append(current)

    return primes_recursive(n, current + 1, primes_list)

def main():
    try:
        n = int(input("Por favor, digite um número maior que 1: "))
        print("Primos (linear):", primes_linear(n))
        print("Primos (recursivo):", primes_recursive(n))
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()