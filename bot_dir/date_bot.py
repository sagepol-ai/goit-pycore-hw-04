# Додавання контакту
def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage: add [name] [phone]"
    name, phone = args
    name = name.capitalize() 

    # використовуємо show_phone для перевірки існування контакту
    exists = show_phone([name], contacts)
    if exists != f"Contact '{name}' not found.":
        return "Contact already exists. Use 'change' to update."

    contacts[name] = phone
    return "Contact added."

# Зміна контакту
def change_contact(args, contacts):
    if len(args) != 2:
        return "Usage: change [name] [new phone]"
    name, phone = args
    name = name.capitalize()             
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact '{name}' not found."


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
