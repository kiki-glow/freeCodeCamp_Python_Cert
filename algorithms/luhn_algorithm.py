def verify_card_number(card_number):
    # Remove spaces and hyphens
    cleaned = card_number.replace(' ', '').replace('-', '')
    
    # Check if all characters are digits
    if not cleaned.isdigit():
        return "INVALID!"
    
    # Convert to list of integers
    digits = [int(d) for d in cleaned]
    
    # Reverse digits for Luhn algorithm
    reversed_digits = digits[::-1]
    
    total = 0
    for i, d in enumerate(reversed_digits):
        if i % 2 == 1:  # Every second digit from the right
            d *= 2
            if d > 9:
                d -= 9  # Equivalent to summing the digits (e.g., 16 → 1+6 → 7)
        total += d
        # print(total)

    # Return the required strings based on checksum
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"   
    
if __name__ == "__main__":
    card_number = '4242 4242 4242 4242'
    print(verify_card_number(card_number))