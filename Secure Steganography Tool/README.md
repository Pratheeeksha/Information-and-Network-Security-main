# Secure Steganography Tool

# Overview

The Secure Steganography Tool is a Python-based application that allows users to securely hide messages inside images using Least Significant Bit (LSB) Steganography and AES encryption. This ensures both confidentiality and covert communication, making the message retrieval possible only with the correct decryption key.

# Features

AES Encryption: Encrypts the message before embedding it in the image.

LSB Steganography: Hides the encrypted message within an image without noticeable distortion.

Secure Key Management: Generates and stores a unique AES key for each encoding session.

Graphical User Interface (GUI): Provides a user-friendly experience using Tkinter.

Manual Key Entry for Decoding: Users need to input the correct AES key to retrieve the hidden message.

# Installation

# Prerequisites

Ensure you have Python installed on your system. You will also need the following libraries:

pip install cryptography opencv-python numpy pillow tkinter

# Running the Application

Clone or download the repository.

Navigate to the project directory and run:

python steganography_tool.py

The GUI will launch, allowing you to encode and decode messages.

# Usage

Encoding a Message

Upload an Image: Click the "Upload Image" button and select an image.

Enter a Message: Type your secret message in the text box.

Encode: Click "Encode Message" to encrypt and embed the message in the image.

Save the Image: The encoded image is saved as encoded_image.png, and the AES key is stored in aes_key.txt.

Decoding a Message

Upload Encoded Image: Click "Decode Message" and select the previously encoded image.

Enter AES Key: Provide the correct key stored in aes_key.txt.

Retrieve Message: If the key is correct, the decrypted message will be displayed.

Google Colab Link: https://colab.research.google.com/drive/1kGtIptK464BvcSG7CXgQ7oIamTuD1Wh_?usp=sharing

# Security Considerations

The AES key must be securely stored and not shared with unauthorized users.

Without the correct AES key, decryption is not possible, ensuring high data security.

LSB steganography modifies pixel values minimally, preventing detection by casual inspection.

# Future Improvements

Enhanced Encryption: Introduce multi-layered encryption for added security.

Multiple Image Format Support: Extend compatibility beyond PNG and JPG.

Cloud Integration: Enable remote encoding and decoding.

Mobile App Version: Develop an Android/iOS application for accessibility.

# License

This project is open-source and available for use and modification under the MIT License.

Acknowledgments

Python Cryptography Library: https://cryptography.io/en/latest/

OpenCV: https://opencv.org/

Tkinter Documentation: https://docs.python.org/3/library/tkinter.html

