# Ваше друге завдання полягає в обчисленні значення інтеграла функції методом Монте-Карло.


import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Визначення функції
def f(x):
    return x ** 2

# Кількість випадкових точок для генерації
n = 100000

# Генерування випадкових значень x та y
x_rand = np.random.uniform(a, b, n)
y_rand = np.random.uniform(0, max(y), n)

# Обчислення кількості точок, які під кривою
points_under_curve = sum(1 for i in range(n) if y_rand[i] <= f(x_rand[i]))

# Обчислення площі прямокутника
rectangle_area = (b - a) * max(y)

# Обчислення відношення площі під кривою до площі прямокутника
integral_approximation = rectangle_area * (points_under_curve / n)

print("Значення інтеграла методом Монте-Карло:", integral_approximation)

# Обчислення точного значення інтеграла за допомогою quad
exact_integral_value, _ = quad(f, a, b)

print("Точне значення інтеграла (використовуючи quad):", exact_integral_value)

# Порівняння результатів
if np.isclose(integral_approximation, exact_integral_value, rtol=1e-5):
    conclusion = "Результати збігаються з точним значенням інтеграла."
else:
    conclusion = "Результати не збігаються з точним значенням інтеграла."

print("Висновок:", conclusion)