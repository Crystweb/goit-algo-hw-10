# Компанія виробляє два види напоїв: "Лимонад" і "Фруктовий сік". Для виробництва цих напоїв використовуються різні
# інгредієнти та обмежена кількість обладнання. Задача полягає у максимізації виробництва, враховуючи обмежені ресурси.
# Використовуючи PuLP, створіть модель, яка визначає, скільки "Лимонаду" та "Фруктового соку" потрібно виробити для
# максимізації загальної кількості продуктів, дотримуючись обмежень на ресурси. Напишіть програму, код якої максимізує
# загальну кількість вироблених продуктів "Лимонад" та "Фруктовий сік", враховуючи обмеження на кількість ресурсів.


from pulp import LpMaximize, LpProblem, LpVariable

# Створення моделі
model = LpProblem(name="maximize_production", sense=LpMaximize)

# Визначення змінних рішення
lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

# Додавання обмежень на ресурси
water_limit = 2 * lemonade + fruit_juice <= 100
sugar_limit = lemonade <= 50
lemon_juice_limit = lemonade <= 30
fruit_puree_limit = 2 * fruit_juice <= 40

# Додавання обмежень до моделі
model += water_limit
model += sugar_limit
model += lemon_juice_limit
model += fruit_puree_limit

# Функція максимізації (максимізація виробництва)
model += lemonade + fruit_juice

# Розв'язання моделі
model.solve()

# Виведення результатів
print("Кількість 'Лимонаду':", lemonade.varValue)
print("Кількість 'Фруктового соку':", fruit_juice.varValue)
