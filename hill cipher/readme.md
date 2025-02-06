# Hill Cipher Encryption

## Description
This Python program implements the **Hill Cipher**, a classical encryption technique based on linear algebra. The Hill Cipher encrypts blocks of text by multiplying vectors of plaintext (converted to numerical values) by an encryption key matrix and taking the result modulo 26. The implementation uses the NumPy library for efficient matrix operations.

## Features
- **Matrix-Based Encryption:** Uses matrix multiplication for encrypting blocks of text.
- **Dynamic Padding:** Automatically pads the plaintext with 'X' if its length is not a multiple of the key matrix size.
- **Case Handling:** Converts plaintext to uppercase and removes spaces.
- **Configurable Key Matrix:** Easily change the encryption key by modifying the key matrix.

## Prerequisites
- Python 3.x
- [NumPy](https://numpy.org/) library

To install NumPy, run:
pip install numpy

How to Run
Clone or Download the Script:
Save the Python script file (e.g., hill_cipher.py) in your working directory.

Navigate to the Project Directory:

cd path/to/your/project
Run the Script:
The program will output the encrypted ciphertext for the given plaintext and key matrix.

Code Explanation
Hill Cipher Encryption Function
Function Name: hill_cipher_encrypt(plaintext, key_matrix)
Parameters:
plaintext: The message to be encrypted.
key_matrix: A NumPy array representing the encryption key.
Steps:
Preprocessing:
Converts the plaintext to uppercase.
Removes spaces.
Pads the plaintext with 'X' to ensure its length is a multiple of the key matrix size.
Text Conversion:
Converts each character to a corresponding number (A=0, B=1, …, Z=25).
Encryption Process:
Splits the plaintext into blocks matching the key matrix size.
Encrypts each block by multiplying it with the key matrix and taking the modulo 26 of the result.
Result Formation:
Converts the numerical ciphertext back into characters and concatenates them to form the final ciphertext.
Example Key Matrix
The provided example uses a 3x3 key matrix:


key_matrix = np.array([[6, 24, 1],
                       [13, 16, 10],
                       [20, 17, 15]])
Example Execution
The script uses the following example to demonstrate the encryption:

python
Copy
Edit
plaintext = "pratheeksha"
print("Encrypted:", hill_cipher_encrypt(plaintext, key_matrix))
When you run the script, the program prints the encrypted message.