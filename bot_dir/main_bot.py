from pathlib import Path
import sys

# шлях до поточної директорії, де знаходиться main_bot.py
current_dir = Path(__file__).parent

# щоб бачити сусідні модулі
if str(current_dir) not in sys.path:
    sys.path.append(str(current_dir))

#імпортуємо необхідні функції з інших модулів
from parse_bot import read_message
from speak_bot import handle_speak
from date_bot import add_contact, change_contact, show_phone, show_all


def main():
    contacts = {}
    started = False
    handle_speak("welcome")  # привітання
# основний цикл бота
    while True:
        user_input = input("Enter a command: ")
        result, started, args = read_message(user_input, started)

        if result in ["close", "exit"]:                 # вихід з бота
            handle_speak("goodbye")
            break

        elif result == "Start":                 # початок роботи бота       
            handle_speak("start")

        elif result == "help":            # допомога користувачу
            handle_speak("help")

        elif result == "add":            # додавання контакту
            handle_speak("add", add_contact(args, contacts))

        elif result == "change":        # зміна контакту
            handle_speak("change", change_contact(args, contacts))

        elif result == "phone":     # показати номер телефону контакту
            handle_speak("phone", show_phone(args, contacts))

        elif result == "all":       # показати всі контакти
            handle_speak("all", show_all(contacts))

        elif result == "hello":     # повторне привітання
            handle_speak("start")

        else:                 # обробка помилок
            handle_speak("error", result)


if __name__ == "__main__":
    main()