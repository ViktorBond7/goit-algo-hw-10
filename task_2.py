import random
import scipy.integrate as spi
from visualize_integral import visualize_integral


def f(x):
        return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

visualize_integral(f, a, b)


# Обчислення інтеграла
result, error = spi.quad(f, a, b)
print("Інтеграл: ", result, error)

def monte_carlo_integral(f, a, b, n=5000):
    total = 0
    for _ in range(n):
        x = random.uniform(a, b)
        total += f(x)
    return (b - a) * total / n

# Тестуємо
result_monte_carlo = monte_carlo_integral(f, a, b)
print(f"Оцінка інтеграла методом Монте-Карло: {result_monte_carlo}")