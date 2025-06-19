import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# Визначення змінних
A = pulp.LpVariable("Лимонад", lowBound=0, cat='Integer')
B = pulp.LpVariable("Фруктовий сік", lowBound=0, cat='Integer')

# Функція цілі (Максимізація прибутку)
model += A + B, "Profit"

# Додавання обмежень
model += A * 2 + B * 2 <= 100  # обмеження по воді
model += A * 1 <= 50           # обмеження по цукру
model += A * 1 <= 30           # обмеження по лимонному соку
model += B * 2 <= 40           # обмеження по фруктовому пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Максимальна кількість пр-ції")
print(f"    Лимонаду: {A.varValue:.0f} одиниць")
print(f"    Фруктового соку: {B.varValue:.0f} одиниць")
