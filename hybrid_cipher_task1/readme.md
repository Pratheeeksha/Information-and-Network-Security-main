1. Vigenère Cipher (Substitution)
## What it does? 
Replaces each letter in the plaintext with a shifted letter based on a repeating key.

## Example:
Plaintext: "HELLO"
Key: "KEY"
Encrypted Text: "RIJVS"


## Encryption Process:
Each letter of the plaintext is shifted forward by the corresponding letter in the key.
The shift is determined by the position of the letter in the alphabet.

## Decryption Process:
Each letter of the ciphertext is shifted backward using the same key.

2. Columnar Transposition Cipher (Rearranging)


## What it does? 

Rearranges the encrypted text based on a keyword.

## Example:

Encrypted Text: "RIJVS"
Key: "CIPHER"
Rearranged Text: Changes the order of letters in a systematic way.


##  Encryption Process:
The text is written in rows based on the key length.
The columns are then rearranged in a specific order determined by sorting the key.


## Decryption Process:
The text is reshuffled back to its original order before applying Vigenère decryption.


3. Hybrid Cipher (Combining Both)

Step 1: Apply Vigenère Cipher to substitute letters.
Step 2: Apply Columnar Transposition Cipher to rearrange the letters.


## Example

## Encryption
Plaintext: "HELLOWORLD"
Step 1: Vigenère Encryption → "RIJVSUYVJN"
Step 2: Columnar Transposition Encryption → Scrambled text (depends on key)

## Decryption
Step 1: Columnar Transposition Decryption → "RIJVSUYVJN"
Step 2: Vigenère Decryption → "HELLOWORLD"


## Why is this more secure?
Vigenère Cipher alone is vulnerable to frequency analysis attacks.
Columnar Transposition Cipher makes it harder to detect patterns.
Combining both increases encryption strength because attackers must break both ciphers, making decryption without a key much more difficult.


## Worked Example to visualise its working 



## Step 1: Given Data

Plaintext: "HELLOWORLD"
Vigenère Key: "SECRETKEY"
Columnar Transposition Key: "KEY"

## Step 2: Vigenère Cipher Encryption (Substitution)
Each letter in "HELLOWORLD" is shifted using the key "SECRETKEY".

## How the Shift Works:
Convert each letter of Vigenère key to a shift value:

S = 18, E = 4, C = 2, R = 17, E = 4, T = 19, K = 10, E = 4, Y = 24


Shift each letter in the plaintext:

H (7) + S (18) = Z (25)
E (4) + E (4) = I (8)
L (11) + C (2) = N (13)
L (11) + R (17) = C (2)
O (14) + E (4) = S (18)
W (22) + T (19) = P (15)
O (14) + K (10) = Y (24)
R (17) + E (4) = V (21)
L (11) + Y (24) = J (9)
D (3) + S (18) = V (21)


Vigenère Encrypted Text: "ZINCSPYVJV"


## Step 3: Columnar Transposition Encryption (Rearranging)

Columnar Transposition Key = "KEY"
Assign numbers based on alphabetical order of key:


K -> 2
E -> 1
Y -> 3


Key Order: E (1st), K (2nd), Y (3rd)

Write the text in a grid (Key Length = 3):


Z  I  N
C  S  P
Y  V  J
V  X  X   (Added 'X' for padding)



Rearrange columns based on key order "KEY" (1 → 2 → 3):


I  Z  N
S  C  P
V  Y  J
X  V  X


Read column-wise to get final encrypted text:
Ciphertext: "ISVXZCVYJPXN"

## Step 4: Decryption (Reverse Process)
Columnar Transposition Decryption

Reconstruct the grid using "KEY"
Read row-wise to get Vigenère text "ZINCSPYVJV"
Vigenère Decryption

Shift each letter backward using "SECRETKEY"
Recover Plaintext: "HELLOWORLD"


output image:
![alt text](image.png)