# 📜 Caesar Cipher Encrypter

This project is a simple Caesar cipher program that allows users to encrypt and decrypt messages with a shift value. It utilizes a looping mechanism that prompts the user to either encode or decode messages repeatedly.

## 📋 Features
- 🔒 **Encode and Decode**: Encrypt messages or decrypt them back to their original form.
- 🔄 **Wrap Around Alphabet**: Handles shifts that go beyond the length of the alphabet.
- ⚡ **User Friendly**: Easy prompts guide you through encoding and decoding.
- 🎨 **Artistic Logo**: Enjoy a visually appealing logo displayed at the start.

## 🛠️ Getting Started

### 1. Clone the Repository
To get started, clone the repository using Git:
```bash
git clone https://github.com/ry8k/Caesar-Cipher-Encrypter
cd Caesar-Cipher-Encryper
```

### 2. Install Required Libraries
Ensure you have the required library:
```bash
none
```

### 3. Run the Program
Execute the Python script to start using the Caesar cipher encrypter:
```bash
python main.py
```

## 📝 Code Overview
Here's how the caeser function works:

```python
def caeser(plain_text, shift_amount, direction):
    # Encrypt or decrypt based on the direction specified
    if direction == "encode":
        # Logic to shift letters for encoding
    elif direction == "decode":
        # Logic to shift letters for decoding
    else:
        print("Please enter a valid option.")
```

## 🔧 Usage
After running the program, follow these simple steps:
- Choose to **encode** or **decode** a message.
- Input your text.
- Provide a **shift number** for the cipher.
- Review your encoded/decoded output! 

## 🔄 Try Again
Would you like to encode or decode another message? Simply confirm when prompted! 

👉 Enjoy using the Caesar Cipher Encrypter! If you have any questions or feedback, feel free to reach out.
