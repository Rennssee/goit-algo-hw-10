from pulp import LpProblem, LpMaximize, LpVariable

# Створюємо модель оптимізації
model = LpProblem(name="Production_Optimization", sense=LpMaximize)

# Оголошуємо змінні рішення - кількість "Лимонаду" та "Фруктового соку"
x1 = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
x2 = LpVariable(name="FruitJuice", lowBound=0, cat="Integer")

# Функція мети - максимізація виробництва
model += x1 + x2, "TotalProduction"

# Додаємо обмеження на використані ресурси
model += 2 * x1 + x2 <= 100, "WaterConstraint"
model += x1 <= 50, "SugarConstraint"
model += x1 <= 30, "LemonJuiceConstraint"
model += 2 * x2 + x1 <= 40, "FruitPureeConstraint"

# Розв'язуємо задачу оптимізації
model.solve()

# Виводимо результати
print(f"Optimal quantity of Lemonade: {x1.value()}")
print(f"Optimal quantity of Fruit Juice: {x2.value()}")
print(f"Maximum total production: {model.objective.value()}")
