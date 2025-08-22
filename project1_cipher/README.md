# 🔐 Vigenère Cipher in Python

This project demonstrates how to **encrypt and decrypt text** using the classical **Vigenère cipher**.  
It was created for the **Summer Coding Class** as a learning project.

---

## 📌 What is the Vigenère Cipher?
The Vigenère cipher is a method of encrypting text using a repeating keyword.  
Each letter of the message is shifted according to the corresponding letter in the key.  

- **Encryption**: Shifts letters **forward** based on the key.  
- **Decryption**: Shifts letters **backward** using the same key.  

---

## 🗂 Project Structure
```
📁 python-vigenere-cipher
│── main.py        # Contains the encryption & decryption code
│── README.md      # Project documentation
```

---

## ⚡ How to Use

### 1. Encrypt a Message
Open `main.py` and set your message and key:
```python
custom_message = "hello world"
custom_key = "python"

encrypted = encrypt(custom_message, custom_key)
print(f"Encrypted message: {encrypted}")
```

### 2. Decrypt a Message
To decrypt the encrypted message:
```python
decrypted = decrypt(encrypted, custom_key)
print(f"Decrypted message: {decrypted}")
```

---

## ▶️ Example Run

### Input Code:
```python
text = "mrttaqrhknsw ih puggrur"
custom_key = "python"

# Decrypt text
decrypted = decrypt(text, custom_key)
print(f"Decrypted text: {decrypted}")

# Encrypt new text
new_message = "summer coding class"
encrypted_new = encrypt(new_message, custom_key)
print(f"Encrypted text: {encrypted_new}")
```

### Output:
```
Decrypted text: summer coding class
Encrypted text: mrttaqrhknsw ih puggrur
```

---

## 🚀 Running the Program
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/python-vigenere-cipher.git
   cd python-vigenere-cipher
   ```
2. Run the script:
   ```bash
   python main.py
   ```

---

## 📝 Notes
- Works only on lowercase `a-z` characters.  
- Spaces and punctuation are not changed.  
- If the key is shorter than the message, it repeats itself.  

---

## 📚 Learn More
- [Vigenère Cipher - Wikipedia](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

---
✨ Practice encrypting and decrypting your own secret messages!
