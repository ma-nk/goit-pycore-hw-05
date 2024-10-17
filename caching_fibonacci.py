def caching_fibonacci(number: int):
    cache = {}

    def fibonacci(n: int):
        if n in cache:
            return cache[n]
        elif n <= 0:
            return 0
        elif n == 1:
            return 1

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci(number)


# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(caching_fibonacci(10))  # Виведе 55
print(caching_fibonacci(15))  # Виведе 610
