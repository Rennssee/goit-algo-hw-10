import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції та межі інтегрування
def f(x):
    return np.sin(x)

a = 0  # Нижня межа
b = 2 * np.pi  # Верхня межа

# Кількість точок, які будемо генерувати
num_points = 100000

# Генерація випадкових точок в прямокутній області
x_points = np.random.uniform(a, b, num_points)
y_points = np.random.uniform(0, max(f(x_points)), num_points)

# Обчислення кількості точок, які потрапили під криву
points_under_curve = sum(y_points <= f(x_points))

# Обчислення площі прямокутника та площі під кривою
total_area = (b - a) * max(f(x_points))
area_under_curve = total_area * (points_under_curve / num_points)

# Виведення результатів методу Монте-Карло
print("Площа під кривою (за допомогою методу Монте-Карло):", area_under_curve)

# Обчислення інтеграла за допомогою quad
result, error = spi.quad(f, a, b)

# Виведення аналітичного результату
print("Аналітичний результат (за допомогою quad):", result)

# Побудова графіка для ілюстрації
x = np.linspace(a, b, 400)
y = f(x)

plt.plot(x_points, y_points, 'bo', alpha=0.5, label='Points')
plt.plot(x, y, 'r', linewidth=2, label='f(x) = sin(x)')
plt.fill_between(x, y, color='gray', alpha=0.3, label='Area under curve')
plt.title('Monte Carlo Integration')
plt.legend()
plt.show()
