# Secure File Encryption System

This project implements a **Secure File Encryption and Decryption System** using **ChaCha20 encryption** to ensure file confidentiality. The system allows users to encrypt and decrypt files via a graphical user interface (GUI) built with **Tkinter**. 

## Features
- **File Encryption**: Files are encrypted using the ChaCha20 cipher with a 256-bit key.
- **File Decryption**: Encrypted files can be decrypted back to their original form with the correct decryption key.
- **Graphical User Interface (GUI)**: The application provides an easy-to-use interface for file encryption and decryption.
  
## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Aaronx1276/encryption-system.git

2. **Navigate into the project directory**:
   ```bash
   cd encryption-system

3. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv

4. **Activate the virtual environment**:
   ```bash
   venv\Scripts\activate

5. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt

6. **Run the application: Start the application by running the following command**:
   ```bash
   python gui.py
   
**Folder Structure**:
1. encryption-system/
2. ├── encryption_utils.py             # Functions for file encryption and decryption
3. ├── decrypted_files/                # Folder where decrypted files are saved
4. ├── encrypted_files/                # Folder where encrypted files are stored
5. ├── gui.py                          # Main GUI file
6. ├── requirements.txt                # Dependencies for the project
7. └── README.md                       # This file

**Feel free to fork, clone, or contribute to the project!**

### Key Sections Explained:
1. **Project Overview**: Focuses on file encryption and decryption with ChaCha20 encryption.
2. **Installation Instructions**: Steps to set up the project environment and install dependencies.
3. **Usage Instructions**: Describes how to use the encryption and decryption features in the GUI.
4. **Folder Structure**: Details the organization of files within the project.
5. **Dependencies**: Lists required Python libraries, with instructions to install them.
6. **License**: You can choose an open-source license like MIT if you wish.
7. **Acknowledgements**: Credits to ChaCha20 encryption.

This `README.md` file should now better reflect the core functionality of your encryption/decryption project. You can update the content as needed.

**Screenshots**:
![image](https://github.com/user-attachments/assets/621cadf2-0916-47ca-9f18-79fce6863c7c)

![image](https://github.com/user-attachments/assets/aa1beb19-b2be-4600-ace4-e685098a7cce)

![image](https://github.com/user-attachments/assets/ba777651-de27-45cc-bd67-5d6051dbac3e)



