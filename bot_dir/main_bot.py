from pathlib import Path
import sys

# шлях до поточної директорії, де знаходиться main_bot.py
current_dir = Path(__file__).parent

# щоб бачити сусідні модулі
if str(current_dir) not in sys.path:
    sys.path.append(str(current_dir))


from parse_bot import read_message
from speak_bot import handle_speak
from date_bot import add_contact, change_contact, show_phone, show_all


def main():
    contacts = {}
    started = False
    handle_speak("welcome")  # привітання

    while True:
        user_input = input("Enter a command: ")
        result, started, args = read_message(user_input, started)

        if result in ["close", "exit"]:
            handle_speak("goodbye")
            break

        elif result == "Start":
            handle_speak("start")

        elif result == "add":
            handle_speak("add", add_contact(args, contacts))

        elif result == "change":
            handle_speak("change", change_contact(args, contacts))

        elif result == "phone":
            handle_speak("phone", show_phone(args, contacts))

        elif result == "all":
            handle_speak("all", show_all(contacts))

        elif result == "hello":
            handle_speak("start")

        else:
            handle_speak("error", result)


if __name__ == "__main__":
    main()