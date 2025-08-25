def verify_card_number(card_number):
    # Initialize the sum for digits in odd positions (from the right)
    sum_of_odd_digits = 0
    
    # Reverse the card number to process from right to left
    card_number_reversed = card_number[::-1]
    
    # Extract digits in odd positions (index 0, 2, 4...) after reversing
    odd_digits = card_number_reversed[::2]

    # Add up all the odd-position digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Initialize the sum for digits in even positions
    sum_of_even_digits = 0
    
    # Extract digits in even positions (index 1, 3, 5...) after reversing
    even_digits = card_number_reversed[1::2]
    
    for digit in even_digits:
        number = int(digit) * 2  # Double each even-position digit
        if number >= 10:  # If result is two digits, add them together (e.g., 12 → 1 + 2 = 3)
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number  # Add to total sum of even digits
    
    # Final sum of odd and even digits
    total = sum_of_odd_digits + sum_of_even_digits
    
    print(total)  # Debugging: print the total sum
    
    # Card is valid if total is divisible by 10 (Luhn algorithm)
    return total % 10 == 0


def main():
    # Example card number (contains dashes for readability)
    card_number = '4111-1111-4555-1141'
    
    # Create a translation table to remove '-' and spaces
    card_translation = str.maketrans({'-': '', ' ': ''})
    
    # Apply translation to clean the card number
    translated_card_number = card_number.translate(card_translation)

    # Verify card number and print result
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


# Run the program
main()
