
sms_normalized = []
bad_numbers = []

def normalize_phone(phone_number: str) -> str | None:                             # Function to normalize Ukrainian phone numbers
    global bad_numbers
    global sms_normalized
    import re

    if phone_number is None:                                                      # Handle None input
        bad_numbers.append(phone_number)
        return None

   
    phone_number_cleaned = re.sub(r"[^+\d]", "", str(phone_number))               # Remove non-digit and non-plus characters

    
    if phone_number_cleaned.count('+') > 1:                                        # Handle multiple plus signs
        phone_number_cleaned = '+' + phone_number_cleaned[1:].replace('+', '')

    normalized = None                                                               # Initialize normalized variable   
    
    if re.match(r'^\+380\d{9}$', phone_number_cleaned):                                # Match +380XXXXXXXXX format
        normalized = phone_number_cleaned

    elif re.match(r'^380\d{9}$', phone_number_cleaned):                                 # Match 380XXXXXXXXX format
        normalized = '+' + phone_number_cleaned

    elif re.match(r'^00380\d{9}$', phone_number_cleaned):                                # Match 00380XXXXXXXXX format
        normalized = '+' + phone_number_cleaned[2:]

    elif re.match(r'^0\d{9}$', phone_number_cleaned):                                    # Match 0XXXXXXXXX format 
        normalized = '+38' + phone_number_cleaned

   
    if normalized:
        if normalized not in sms_normalized:                                            # Avoid duplicates  
            sms_normalized.append(normalized)
        return normalized

    
    bad_numbers.append(phone_number)                                                      # Collect bad numbers
    return None  
