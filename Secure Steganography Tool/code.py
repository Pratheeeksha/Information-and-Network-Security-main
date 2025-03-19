import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import numpy as np
import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from PIL import Image, ImageTk

# Global variables
image_path = None
aes_key = None

# AES Functions
def generate_aes_key():
    """Generate a 16-byte AES key."""
    return os.urandom(16)

def save_key(key):
    """Save AES key to a text file."""
    with open("aes_key.txt", "wb") as f:
        f.write(key)

def load_key():
    """Load AES key from a text file."""
    if not os.path.exists("aes_key.txt"):
        messagebox.showerror("Error", "AES key file not found! Use the correct key.")
        return None
    with open("aes_key.txt", "rb") as f:
        return f.read()

def encrypt_message(message, key):
    """Encrypts a message using AES."""
    message_bytes = message.encode()  
    padder = padding.PKCS7(128).padder()  
    padded_message = padder.update(message_bytes) + padder.finalize()

    iv = os.urandom(16)  
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(padded_message) + encryptor.finalize()

    return base64.b64encode(iv + encrypted_message).decode()  

def decrypt_message(encrypted_message, key):
    """Decrypts a message using AES."""
    try:
        encrypted_bytes = base64.b64decode(encrypted_message)
        iv = encrypted_bytes[:16]  
        encrypted_data = encrypted_bytes[16:]

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        decrypted_padded = decryptor.update(encrypted_data) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        decrypted_message = unpadder.update(decrypted_padded) + unpadder.finalize()

        return decrypted_message.decode()
    except:
        messagebox.showerror("Error", "Decryption failed! Wrong key or corrupted image.")
        return None

# Steganography Functions
def text_to_binary(text):
    """Converts text to binary."""
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary_string):
    """Converts binary data back to readable text."""
    chars = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def encode_message(image, message):
    """Encodes a secret message into the image using LSB technique."""
    message += "####"  
    binary_message = text_to_binary(message)
    message_length = len(binary_message)
    
    flat_image = image.flatten()
    if message_length > len(flat_image):
        messagebox.showerror("Error", "Message is too long for the image!")
        return None

    for i in range(message_length):
        flat_image[i] = (flat_image[i] & 0xFE) | int(binary_message[i])  
    
    return flat_image.reshape(image.shape)

def decode_message(image):
    """Extracts the hidden message from the image."""
    flat_image = image.flatten()
    binary_message = ''

    for pixel in flat_image:
        binary_message += str(pixel & 1)  

    message = binary_to_text(binary_message)
    return message.split("####")[0]  

# GUI Functions
def upload_image():
    """Open file dialog to select an image."""
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    
    if image_path:
        messagebox.showinfo("Success", "Image uploaded successfully!")
        display_image(image_path)

def display_image(img_path):
    """Display selected image in the GUI."""
    img = Image.open(img_path)
    img = img.resize((300, 300))
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img  

def encode():
    """Encrypt and encode the message into the image."""
    global aes_key
    if not image_path:
        messagebox.showerror("Error", "Please upload an image first!")
        return

    message = text_entry.get("1.0", tk.END).strip()
    if not message:
        messagebox.showerror("Error", "Please enter a message!")
        return

    aes_key = generate_aes_key()
    save_key(aes_key)  # Save AES key

    encrypted_message = encrypt_message(message, aes_key)

    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    encoded_image = encode_message(image, encrypted_message)
    if encoded_image is None:
        return

    cv2.imwrite("encoded_image.png", cv2.cvtColor(encoded_image, cv2.COLOR_RGB2BGR))
    messagebox.showinfo("Success", "Message encoded and saved as encoded_image.png!\nAES Key saved in aes_key.txt")

def decode():
    """Decode and decrypt the hidden message from an image."""
    encoded_image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png")])
    if not encoded_image_path:
        return

    encoded_image = cv2.imread(encoded_image_path)
    encoded_image = cv2.cvtColor(encoded_image, cv2.COLOR_BGR2RGB)

    retrieved_message = decode_message(encoded_image)
    if not retrieved_message:
        messagebox.showerror("Error", "No hidden message found!")
        return

    aes_key = load_key()
    if aes_key is None:
        return

    decrypted_message = decrypt_message(retrieved_message, aes_key)
    if decrypted_message:
        messagebox.showinfo("Decoded Message", f"🔓 Hidden Message:\n{decrypted_message}")

# GUI Layout
root = tk.Tk()
root.title("Secure Steganography Tool")
root.geometry("500x600")

# Upload Button
upload_btn = tk.Button(root, text="Upload Image", command=upload_image, font=("Arial", 12))
upload_btn.pack(pady=10)

# Display Image
image_label = tk.Label(root)
image_label.pack()

# Message Entry
text_entry = tk.Text(root, height=5, width=50)
text_entry.pack()

# Encode & Decode Buttons
encode_btn = tk.Button(root, text="Encode Message", command=encode, font=("Arial", 12))
encode_btn.pack(pady=5)

decode_btn = tk.Button(root, text="Decode Message", command=decode, font=("Arial", 12))
decode_btn.pack(pady=5)

root.mainloop()
