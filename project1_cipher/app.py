# Python Projects
# This repo will contain all python projects from the summer coding class 

# Encrypted text to be decrypted
text = 'mrttaqrhknsw ih puggrur'
# Key used for Vigenère cipher
custom_key = 'happycoding'

# Function to perform Vigenère encryption or decryption
def vigenere(message, key, direction=1):
    key_index = 0  # Keeps track of which character of the key to use
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Allowed characters for encryption
    final_message = ''  # Stores the final encrypted/decrypted message

    # Loop through each character in the message
    for char in message.lower():

        # If the character is not a letter (e.g., space, punctuation), add it as is
        if not char.isalpha():
            final_message += char
        else:        
            # Pick the correct key character by cycling through the key
            key_char = key[key_index % len(key)]
            key_index += 1

            # Find the shift value from the key character
            offset = alphabet.index(key_char)
            # Find the position of the current message character
            index = alphabet.find(char)
            # Shift index forward for encryption (direction=1)
            # or backward for decryption (direction=-1)
            new_index = (index + offset * direction) % len(alphabet)
            # Append the new encrypted/decrypted character
            final_message += alphabet[new_index]
    
    return final_message  # Return the final processed message

# Encrypt function (wraps vigenere with direction=1 by default)
def encrypt(message, key):
    return vigenere(message, key)
    
# Decrypt function (wraps vigenere with direction=-1)
def decrypt(message, key):
    return vigenere(message, key, -1)

# Print original encrypted text
print(f'\nEncrypted text: {text}')
# Print the key used
print(f'Key: {custom_key}')
# Decrypt the text using the key
decryption = decrypt(text, custom_key)
# Print the decrypted message
print(f'\nDecrypted text: {decryption}\n')   

