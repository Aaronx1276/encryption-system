import tkinter as tk
from tkinter import filedialog, messagebox
import os
import pyperclip
from encryption_utils import encrypt_file, decrypt_file  # Import functions from encryption_utils.py

# Paths for encrypted and decrypted files
ENCRYPTED_FOLDER = "encrypted_files"
DECRYPTED_FOLDER = "decrypted_files"

# Create folders if they don't exist
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_FOLDER, exist_ok=True)

# Initialize the main window
root = tk.Tk()
root.title("Secure File Sharing")
root.geometry("400x300")

# Function to handle file encryption
def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            file_name = os.path.basename(file_path)
            output_path = os.path.join(ENCRYPTED_FOLDER, file_name + ".enc")
            key = encrypt_file(file_path, output_path)  # Call the encryption function

            # Display the key in terminal
            print(f"Encryption Key: {key}")

            # Automatically copy key to clipboard
            pyperclip.copy(key)
            print("Encryption key copied to clipboard.")

            messagebox.showinfo(
                "Encryption Successful",
                f"File '{file_name}' has been encrypted.\n\nEncryption Key: {key}\n\n"
                "The key has also been copied to your clipboard!"
            )
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to handle file decryption
def decrypt_file_gui():
    file_path = filedialog.askopenfilename(initialdir=ENCRYPTED_FOLDER)
    if file_path:
        try:
            file_name = os.path.basename(file_path)
            output_path = os.path.join(DECRYPTED_FOLDER, file_name.replace(".enc", ""))
            key = simple_input_box("Enter Decryption Key", "Enter the key to decrypt the file:")
            if not key:
                return
            decrypt_file(file_path, output_path, key)  # Call the decryption function
            messagebox.showinfo("Decryption Successful", f"File '{file_name}' has been decrypted.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Simple input box to get key from user
def simple_input_box(title, prompt):
    input_window = tk.Toplevel(root)
    input_window.title(title)
    input_window.geometry("300x100")
    tk.Label(input_window, text=prompt).pack(pady=5)
    key_entry = tk.Entry(input_window, show="*")
    key_entry.pack(pady=5)
    key = tk.StringVar()

    def submit_key():
        key.set(key_entry.get())
        input_window.destroy()

    tk.Button(input_window, text="Submit", command=submit_key).pack(pady=5)
    input_window.wait_window()  # Wait until the window is closed
    return key.get()

# Upload button
upload_button = tk.Button(root, text="Upload and Encrypt File", command=upload_file)
upload_button.pack(pady=20)

# Decrypt button
decrypt_button = tk.Button(root, text="Decrypt File", command=decrypt_file_gui)
decrypt_button.pack(pady=20)

# Run the GUI
root.mainloop()
