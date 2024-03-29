# goit-algo-hw-10

# Висновки щодо обчислення інтегралу методом Монте-Карло

У даному завданні ми використовували метод Монте-Карло для обчислення площі під кривою функції та порівняння результатів з аналітичним обчисленням інтегралу за допомогою функції `quad` з бібліотеки SciPy.

Отримані результати:

- Площа під кривою (за допомогою методу Монте-Карло): 2.0175936338758658
- Аналітичний результат (за допомогою quad): 2.221501482512777e-16

Ми можемо спостерігати, що значення, отримане методом Монте-Карло, не дуже точно відповідає аналітичному результату. Це може бути пов'язано зі статистичною випадковістю методу Монте-Карло та обраною кількістю точок. Значення змінної може коливатися від запуску до запуску.

Завдяки методу Монте-Карло ми можемо отримати наближене значення інтегралу, але для точних результатів рекомендується використовувати аналітичні методи, такі як функція `quad` у бібліотеці SciPy.
