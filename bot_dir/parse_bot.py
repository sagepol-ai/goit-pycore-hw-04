# функція для обробки вхідних повідомлень бота
def read_message(input_message, started):
    message = input_message.strip().lower()

    if not started:      # якщо бот ще не стартував
        if message == "hello":
            return "Start", True, []
        else:
            return "Please write 'hello' to start.", False, []

    else:           # якщо бот вже стартував
        parts = message.split()
        if not parts:
            return "Invalid command.", True, []

        cmd = parts[0]
        args = parts[1:]

        valid_commands = ["add", "change", "phone", "all", "close", "exit", "hello", "help"]                                 

        if cmd in valid_commands:
            return cmd, True, args
        else:
            return "Invalid command.", True, []
