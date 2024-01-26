def decrypt(ciphertext, inverse_key):
    """
    Decrypts a message encrypted using the monoalphabetic substitution cipher
    @param ciphertext: str
    @param inverse_key: dict, the inverse key mapping ciphertext -> plaintext
    @return: str
    """

    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                plaintext += inverse_key[char]
            else:
                plaintext += inverse_key[char.upper()].lower()
        else:
            plaintext += char

    return plaintext






decrypted_message = decrypt(message, inverse_key)


print("Decrypted Message:", decrypted_message)
