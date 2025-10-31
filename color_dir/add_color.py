#!/usr/bin/env python3

import sys
from pathlib import Path
from colorama import Fore, init

# Ініціалізуємо бібліотеку colorama для кольорового виведення в термінал
init(autoreset=True)


def add_color_to_dir(path_color, level=0):
    """
    Рекурсивна функція для відображення структури директорії з кольоровим форматуванням.
    Папки виводяться синім кольором, файли — білим.
    """
    p = Path(path_color)

    # Перевіряємо, чи існує шлях
    if not p.exists():
        print(f"Шлях не існує: {p}")
        return
    
    # Перевіряємо, чи це саме директорія, а не файл
    if not p.is_dir():
        print(f"Це не директорія: {p}")
        return

    # Виводимо назву поточної папки синім кольором
    print('  ' * level + Fore.BLUE + f" {p.name}/")

    # Проходимо по всіх елементах у поточній папці
    for item in p.iterdir():
        if item.is_dir():
            # Якщо це підпапка  викликаємо функцію знову
            add_color_to_dir(item, level + 1)
        else:
            # Якщо це файл виводимо білим кольором
            print('  ' * (level + 1) + Fore.GREEN + f" {item.name}")

# Викликаємо функцію, передаючи шлях, отриманий із командного рядка
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до директорії.")
    else:
        # Отримуємо шлях до директорії з аргументів командного рядка
        path_color = sys.argv[1]
        add_color_to_dir(path_color)

