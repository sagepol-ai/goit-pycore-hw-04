def handle_speak(command, message=None):
    """
    Відповідає за всі повідомлення користувачу
    """
    # словник відповідей
    responses = {
        "welcome": "Welcome to the assistant bot! Send 'hello' to start.",
        "start": "How can I help you? You can add, change, or view contacts.",
        "goodbye": "Good bye!",
        "add": message,
        "change": message,
        "phone": message,
        "all": message,
        "error": message
    }

    # отримуємо відповідь з словника або використовуємо передане повідомлення з main_bot.py
    response = responses.get(command, message)
    if response:
        print(response)
