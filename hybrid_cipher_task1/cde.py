import math

# Vigenère Cipher Functions
def vigenere_encrypt(plaintext: str, key: str) -> str:
    encrypted = []
    key_len = len(key)
    for i, char in enumerate(plaintext.upper()):
        if char.isalpha():
            shift = ord(key[i % key_len].upper()) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted.append(encrypted_char)
    return ''.join(encrypted)

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    decrypted = []
    key_len = len(key)
    for i, char in enumerate(ciphertext.upper()):
        if char.isalpha():
            shift = ord(key[i % key_len].upper()) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted.append(decrypted_char)
    return ''.join(decrypted)

# Columnar Transposition Functions
def get_permutation_order(key: str) -> list[int]:
    sorted_key = sorted([(k, i) for i, k in enumerate(key)], key=lambda x: x[0])
    return [x[1] for x in sorted_key]

def columnar_encrypt(plaintext: str, key: str) -> str:
    key_len = len(key)
    if key_len == 0:
        return plaintext
    perm_order = get_permutation_order(key)
    num_rows = math.ceil(len(plaintext) / key_len)
    padded_text = plaintext.ljust(num_rows * key_len, 'X')
    grid = [padded_text[i*key_len:(i+1)*key_len] for i in range(num_rows)]
    ciphertext = ''.join([grid[row][col] for col in perm_order for row in range(num_rows)])
    return ciphertext

def columnar_decrypt(ciphertext: str, key: str) -> str:
    key_len = len(key)
    if key_len == 0:
        return ciphertext
    perm_order = get_permutation_order(key)
    num_rows = len(ciphertext) // key_len
    chunks = [ciphertext[i*num_rows:(i+1)*num_rows] for i in range(key_len)]
    original_columns = [''] * key_len
    for i, col_idx in enumerate(perm_order):
        original_columns[col_idx] = chunks[i]
    plaintext = ''.join([original_columns[col][row] for row in range(num_rows) for col in range(key_len)])
    return plaintext.rstrip('X')

# Hybrid Cipher Functions
def hybrid_encrypt(plaintext: str, vigenere_key: str, transposition_key: str) -> str:
    vigenere_encrypted = vigenere_encrypt(plaintext, vigenere_key)
    hybrid_encrypted = columnar_encrypt(vigenere_encrypted, transposition_key)
    return hybrid_encrypted

def hybrid_decrypt(ciphertext: str, vigenere_key: str, transposition_key: str) -> str:
    columnar_decrypted = columnar_decrypt(ciphertext, transposition_key)
    hybrid_decrypted = vigenere_decrypt(columnar_decrypted, vigenere_key)
    return hybrid_decrypted

# Example Usage
if __name__ == "__main__":
    # Example 1
    plaintext = input("Enter an plainText: ")
    vigenere_key = input("Enter an key: ")
    transposition_key =input("Enter an transposition_key: ")
    
    encrypted = hybrid_encrypt(plaintext, vigenere_key, transposition_key)
    decrypted = hybrid_decrypt(encrypted, vigenere_key, transposition_key)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}\n")
    
   