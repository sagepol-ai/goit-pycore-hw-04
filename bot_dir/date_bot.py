# Додавання контакту
def add_contact(args, contacts):
    try:
        if len(args) != 2:
            return "Usage: add [name] [phone]"
        name, phone = args
        name = name.capitalize()
        if not phone.isdigit():
            return "Phone number must contain only digits."
        if name in contacts:
            return "Contact already exists. Use 'change' to update."
        contacts[name] = phone
        return "Contact added."
    except Exception as e:
        return f"Unexpected error: {e}"


# Зміна контакту
def change_contact(args, contacts):
    try:
        if len(args) != 2:
            return "Usage: change [name] [new phone]"
        name, phone = args
        name = name.capitalize()
        if name not in contacts:
            return f"Contact '{name}' not found."
        contacts[name] = phone
        return "Contact updated."
    except Exception as e:
        return f"Unexpected error: {e}"


# Показати номер телефону контакту
def show_phone(args, contacts):
    if len(args) != 1:
        return "Usage: phone [name]"
    name = args[0].capitalize()       
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact '{name}' not found."


# Показати всі контакти
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = "Contacts list:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()
