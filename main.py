"""
Crypton-1 - Developed by ErWin

This software has developed for encryption and decryption purposes.
More updates will be announced in the future.

Developed on: 12/01/2022

This is the main part of where every function of the software are ready to use.

"""
import tkinter as tk
import subprocess

# Create the main window.
window = tk.Tk()

# Frame for the window.
frame = tk.Frame(window)
frame.pack()

# Input Field codes.
input_field = tk.Entry(frame , width=50)
input_field.grid(row=0, column=0, padx=20, pady=20, ipadx=20, ipady=5,sticky='nsew')

# Lower text area of the input place.
label = tk.Label(text="For encryption, write a plaintext. For decryption, write the encrypted text. Don't use decryption like this: b'message', use it like this: message ")
label.pack()


# ENCRYPT button.
def encrypt_callback():
    text = input_field.get()
    subprocess.call(["python", "encryption.py", text])    # ---> This function gets the text from input field and passes it directly to encryption.py


encrypt_button = tk.Button(text="ENCRYPT", bg="blue", width=20, height=4, font=("Arial", 16), command=encrypt_callback)
encrypt_button.pack(side="left")


""" // Section 2 // """

# DECRYPT button.

def decrypt_callback():
    text = input_field.get()
    subprocess.call(["python", "decryption.py", text])    # ---> Works same as the ENCRYPT button.

decrypt_button = tk.Button(text="DECRYPT", bg="red", width=20, height=4, font=("Arial", 16), command=decrypt_callback)
decrypt_button.pack(side="right")


# Run the tkinter event loop.
window.mainloop()