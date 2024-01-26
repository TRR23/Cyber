def decrypt(ciphertext: str, inverse_key: dict[str, str]) -> str:
    """
    Decrypts a message encrypted using the monoalphabetic substitution cipher
    @param ciphertext: str
    @param inverse_key: dict[str, str], the inverse key mapping ciphertext -> plaintext
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


def get_inverse_key(key: dict[str, str]) -> dict[str, str]:
    """
    reverses dictionary mapping
    @param key: dict[str, str]
    @return: dict[str, str]
    """
    inverse_key = {value: key for key, value in key.items()}
    return inverse_key

    
def encrypt(plaintext: str, key: dict[str, str]) -> str:
    """
    Encrypts a message using the monoalphabetic substitution cipher
    @param plaintext: str
    @param key: str, the key is represented as a dictionary mapping plaintext -> ciphertext
    @return: str
    """

    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += key[char]
            else:
                ciphertext += key[char.upper()].lower()

        else:
            ciphertext += char

    return ciphertext


key = {'A': 'M', 'B': 'T', 'C': 'V', 'D': 'C', 'E': 'X', 'F': 'A', 'G': 'S', 'H': 'U', 'I': 'H', 'J': 'Z',
       'K': 'Y', 'L': 'P', 'M': 'O', 'N': 'I', 'O': 'W', 'P': 'J', 'Q': 'E', 'R': 'Q', 'S': 'G', 'T': 'L',
       'U': 'K', 'V': 'F', 'W': 'B', 'X': 'R', 'Y': 'D', 'Z': 'N'}


plaintext = "Abraham Lincoln"
ciphertext = encrypt(plaintext, key)


inverse_key = get_inverse_key(key)

decrypted_text = decrypt(ciphertext, inverse_key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
