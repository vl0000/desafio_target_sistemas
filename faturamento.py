import statistics
import sys

# Modifique a entrada aqui!
vector: list = [1234.5, 1943.2, 4032.0, 91.0, 3021.0]


def days_above_mean(fat: list[float]) -> int:
    """Retorna o número de dias em que o faturamento foi maior que a média"""
    mean: float
    # Dias em que o faturamento foi mairo que a média(mean)
    days: int = 0
    try:
        mean = statistics.mean(fat)
    except:
        print("Entrada inválida")
        sys.exit(1)

    for num in fat:
        if num > mean:
            days += 1

    return days


def run(vec: list[float]):
    print(f"Menor faturament: {min(vec)}\nMaior faturament: {max(vec)}\nDias acima da média: {days_above_mean(vec)}")


if __name__ == "__main__":
    run(vector)
