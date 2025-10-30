from pathlib import Path
current_dir = Path(__file__).parent
salary_file = current_dir / 'salaries.txt'
def total_salary(salary_file):
   
    with open(salary_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()  # читаємо всі рядки одразу

    salaries = [int(line.strip().split(',')[1]) for line in lines]
    total = sum(salaries)
    average = total / len(salaries)
    return total, average
total, average = total_salary(salary_file)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")  