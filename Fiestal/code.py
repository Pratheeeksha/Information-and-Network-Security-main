s = input("Enter a string: ")
# Convert string to ASCII and then to 8-bit binary
result = "".join(format(ord(i), '08b') for i in s)
print("Result:", result)

l = len(result) // 2
left = result[:l]
right = result[l:]

k = input("Enter a key: ")
key = "".join(format(ord(i), '08b') for i in k)

# Feistel function
s = bin(int(right, 2) + int(key, 2))[2:]
answer = bin(int(s, 2) ^ int(left, 2))[2:]

# Swap left and right
newr = answer.zfill(len(left))
newl = right
newr, newl = newl, newr

s = bin(int(newr, 2) + int(key, 2))[2:]
ans = bin(int(s, 2) ^ int(newl, 2))[2:]

nl = newr
nr = ans.zfill(len(newl))
nl, nr = nr, nl

cipher = nl + nr

# Padding if cipher length is less than original
cipher = cipher.zfill(len(result))

print("Cipher Text (Binary):", cipher)

# Convert binary to plaintext
plainText = "".join(chr(int(cipher[i:i+8], 2)) for i in range(0, len(cipher), 8))
print("Cipher Text:", plainText)
