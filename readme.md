## Висновки щодо результатів обчислення інтеграла методом Монте-Карло:
Різниця між значеннями, отриманими методом Монте-Карло та точним значенням інтеграла, може бути пов'язана з тим, що метод Монте-Карло ґрунтується на випадковому виборі точок для оцінки площі під кривою. Тому точність результату залежить від кількості випадкових точок, які використовуються для оцінки. Чим більше точок, тим більш точним буде результат, але це може призвести до збільшення обчислювального часу.

З іншого боку, метод quad з бібліотеки SciPy використовує числові методи для обчислення інтеграла, що може бути більш точним, оскільки він розрахований на роботу з функціями. Однак він також може вимагати більше ресурсів обчислювальної машини.

Вибір між цими методами залежить від ваших потреб. Якщо вам потрібна швидка оцінка, яка може бути менш точною, метод Монте-Карло може бути відмінним варіантом. У той же час, якщо вам потрібна вища точність та ви готові змагатися з більшими обчислювальними витратами, метод quad може бути кращим варіантом.

- Значення, отримане методом Монте-Карло: 2.662944.
- Точне значення інтеграла (використовуючи quad): 2.6666666666666665.
- Результати не збігаються з точним значенням інтеграла.