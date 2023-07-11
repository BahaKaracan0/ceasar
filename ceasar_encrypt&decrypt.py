#Ceasar Encrpt & Decrypt

import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

class CaesarEncryption:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Encryption")
        self.root.geometry("400x400")

        # Title Label
        self.title_label = tk.Label(self.root, text="Caesar Encryption", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Text Label
        self.text_label = tk.Label(self.root, text="Text:")
        self.text_label.pack()

        # Text Input
        self.text_input = scrolledtext.ScrolledText(self.root, width=40, height=6, font=("Arial", 12))
        self.text_input.pack()

        # Key Label
        self.key_label = tk.Label(self.root, text="Key:")
        self.key_label.pack()

        # Key Input
        self.key_input = tk.Entry(self.root, font=("Arial", 12))
        self.key_input.pack()

        # Encrypt Button
        self.encrypt_button = tk.Button(self.root, text="Encrypt", command=self.encrypt, font=("Arial", 12, "bold"), bg="lightblue")
        self.encrypt_button.pack(pady=10)

        # Encrypted Text Label
        self.encrypted_text_label = tk.Label(self.root, text="Encrypted Text:")
        self.encrypted_text_label.pack()

        # Encrypted Text Area
        self.encrypted_text_area = scrolledtext.ScrolledText(self.root, width=40, height=6, font=("Arial", 12))
        self.encrypted_text_area.pack()

        # Decrypt Button
        self.decrypt_button = tk.Button(self.root, text="Decrypt", command=self.decrypt, font=("Arial", 12, "bold"), bg="lightgreen")
        self.decrypt_button.pack(pady=10)

        # Decrypted Text Label
        self.decrypted_text_label = tk.Label(self.root, text="Decrypted Text:")
        self.decrypted_text_label.pack()

        # Decrypted Text Area
        self.decrypted_text_area = scrolledtext.ScrolledText(self.root, width=40, height=6, font=("Arial", 12))
        self.decrypted_text_area.pack()

    def encrypt(self):
        text = self.text_input.get("1.0", "end-1c")
        key = self.key_input.get()
        if not key.isdigit():
            messagebox.showerror("Error", "Key must be an integer.")
            return
        key = int(key)
        encrypted_text = self.caesar_encrypt(text, key)
        self.encrypted_text_area.delete("1.0", "end")
        self.encrypted_text_area.insert("1.0", encrypted_text)

    def decrypt(self):
        encrypted_text = self.encrypted_text_area.get("1.0", "end-1c")
        key = self.key_input.get()
        if not key.isdigit():
            messagebox.showerror("Error", "Key must be an integer.")
            return
        key = int(key)
        decrypted_text = self.caesar_decrypt(encrypted_text, key)
        self.decrypted_text_area.delete("1.0", "end")
        self.decrypted_text_area.insert("1.0", decrypted_text)

    def caesar_encrypt(self, text, key):
        """
        Encrypts the text using the Caesar cipher algorithm with the given key.
        """
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    ascii_code = ord(char)
                    ascii_code = (ascii_code - 97 + key) % 26 + 97
                else:
                    ascii_code = ord(char)
                    ascii_code = (ascii_code - 65 + key) % 26 + 65
                encrypted_text += chr(ascii_code)
            else:
                encrypted_text += char
        return encrypted_text

    def caesar_decrypt(self, encrypted_text, key):
        """
        Decrypts the encrypted text using the Caesar cipher algorithm with the given key.
        """
        decrypted_text = ""
        for char in encrypted_text:
            if char.isalpha():
                if char.islower():
                    ascii_code = ord(char)
                    ascii_code = (ascii_code - 97 - key) % 26 + 97
                else:
                    ascii_code = ord(char)
                    ascii_code = (ascii_code - 65 - key) % 26 + 65
                decrypted_text += chr(ascii_code)
            else:
                decrypted_text += char
        return decrypted_text

root = tk.Tk()
caesar_encryption = CaesarEncryption(root)
root.mainloop()
