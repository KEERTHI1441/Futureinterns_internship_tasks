# README.md

# 🔐 Secure File Sharing System

This is a simple, secure file sharing system built using **Python Flask** and **AES encryption**.
Created as part of Cyber Security Task 3 by Future Interns.

## 📑 Project Features

* Secure file upload and download using Flask web framework.
* AES (Advanced Encryption Standard) encryption for files at rest.
* Basic encryption key management using `.env` file.
* User-friendly web interface for file management.
* Separation of encryption logic for clean code organization.

---

## ⚙️ Technology Stack

* Python 3.x
* Flask
* PyCryptodome
* HTML / CSS / JavaScript
* GitHub for version control

---

## 📁 Project Structure

```
secure_file_sharing/
├── app.py
├── encryption.py
├── .env
├── .gitignore
├── templates/
├── static/
├── uploads/
├── decrypted/
├── README.md
├── SECURITY_OVERVIEW.md
```

---

## 🚀 How to Run Locally

### 1️⃣ Install Dependencies

```bash
pip install flask pycryptodome python-dotenv
```

### 2️⃣ Set Encryption Key

Create a `.env` file:

```
ENCRYPTION_KEY=ThisIsASecretKy
```

Key must be **16, 24, or 32 bytes long**.

### 3️⃣ Run Flask App

```bash
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 📸 Screenshots

### Uploading file to encrypt

![Uploading file to encrypt](./assets/uploading.PNG)

### Decrypting the file while downloading

![Decrypting the file while downloading](./assets/downloading.png)

---

## 📹 Walkthrough Video

[Walkthrough Video](https://www.loom.com/share/31c4a908712f4a67b094dd0bf759222b?sid=78a137cb-e08a-4610-81c2-8bb0683ef2c5)

---

## 📄 Security Notes

Refer to `SECURITY_OVERVIEW.md` for encryption methods and key management practices.

