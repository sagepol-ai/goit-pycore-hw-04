# відкриівання файлу cats_list.txt з поточної директорії

from pathlib import Path
current_dir = Path(__file__).parent
cats_file = current_dir / 'cats_list.txt'

def get_cats_info (cats_file):
    cats = []
    try:
        with open(cats_file, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    id, name, age = line.strip().split(',')
                    cats.append({'id': id, 'name': name, 'age': int(age)})
                except ValueError:
                    print(f"Некоректний рядок: № {line_number}, {line.strip()}")
    except FileNotFoundError:
        print(f"Файл {cats_file} не знайдено. Будь ласка, додайте файл cats_list.txt у дерікторію cat_dir.")
    return cats
print(get_cats_info(cats_file))