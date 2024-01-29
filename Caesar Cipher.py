from string import ascii_lowercase

def decrypt_index(ciphertext: str, key: int) -> str:
    """
    Inverse of the Caesar Cipher implemented with indexed collection of English letters
    :param ciphertext: str
    :param key: int
    :return: str
    """

    plaintext = ""
    for char in ciphertext:
        was_upper = char.isupper()

        initial_idx = ascii_lowercase.index(char.lower())
        shifted_idx = (initial_idx - key) % 26

        shifted_char = ascii_lowercase[shifted_idx]

        if was_upper:
            shifted_char = shifted_char.upper()

        plaintext += shifted_char

    return plaintext


    

def encrypt_index(plaintext: str, key: int) -> str:
    """
    Caesar Cipher implemented with indexed collection of english letters
    :param plaintext: str
    :param key: int
    :return: str
    """

    ciphertext = ""
    for char in plaintext:
        was_upper = char.isupper()

        initial_idx = ascii_lowercase.index(char.lower())
        shifted_idx = (initial_idx + key) % 26

        shifted_char = ascii_lowercase[shifted_idx]

        if was_upper:
            shifted_char = shifted_char.upper()

        ciphertext += shifted_char

    return ciphertext
