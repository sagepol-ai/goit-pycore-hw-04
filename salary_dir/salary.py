from pathlib import Path

# Отримуємо шлях до поточної директорії, де знаходиться цей файл
current_dir = Path(__file__).parent

# Формуємо повний шлях до файлу 'salaries.txt' у цій директорії
salary_file = current_dir / 'salaries.txt'


def total_salary(salary_file):
    """
    Функція зчитує файл із зарплатами розробників і повертає
    загальну та середню суму заробітної плати.
    """
    # Відкриваємо файл у режимі читання з кодуванням UTF-8
    with open(salary_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()  # Зчитуємо всі рядки одразу в список

    # Створюємо список із числовими значеннями зарплат
    # Кожен рядок має формат: Ім'я,Зарплата → беремо другий елемент (після коми)
    salaries = [int(line.strip().split(',')[1]) for line in lines]

    # Розраховуємо загальну та середню зарплату
    total = sum(salaries)
    average = total / len(salaries)

    # Повертаємо кортеж із двох значень
    return total, average


# Викликаємо функцію та виводимо результат у зручному форматі
total, average = total_salary(salary_file)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
