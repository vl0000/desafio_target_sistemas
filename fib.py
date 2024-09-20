def fibonacci(n: int):
    """A função calculará a sequencia de Fibonacci até n (inclusivo)"""
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def is_fib(n: int):
    buff: list = []
    for i in range(n + 2):
        buff.append(fibonacci(i))

    print(buff)
    if n in buff:
        print(f"{n} \033[92mé parte da sequencia!\033[39m")
    else:
        print(f"{n} \033[31mnão é parte da sequencia!\033[39m")


num: int = 0

try:
    int(input("Número: "))
    is_fib(num)
except ValueError:
    print("Entrada inválida")
