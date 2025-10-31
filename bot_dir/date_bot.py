def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Usage: change [name] [new phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact '{name}' not found."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact '{name}' not found."


def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = "Contacts list:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()
