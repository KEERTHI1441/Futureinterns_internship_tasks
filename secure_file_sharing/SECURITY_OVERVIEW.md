## 📜 License

For educational purposes only.

# SECURITY\_OVERVIEW\.md

# 🔐 Security Overview

This document explains the security measures implemented in the Secure File Sharing System for Cyber Security Task 3.

---

## ✅ Encryption Method

* **Algorithm:** AES (Advanced Encryption Standard)
* **Mode:** CBC (Cipher Block Chaining)
* **Key Size:** 128 bits (16 bytes)

### ✅ Why AES?

AES is a widely recognized, industry-standard encryption algorithm. CBC mode adds an initialization vector (IV) to enhance security by preventing pattern detection in ciphertext.

---

## ✅ Key Management

* **Storage:**
  Encryption key is stored in a `.env` file and accessed using `python-dotenv`.

* **Security Note:**
  Hardcoding keys in source code is avoided.
  In production environments, keys should be managed using services like:

  * AWS KMS
  * Azure Key Vault
  * HashiCorp Vault

* **Validation:**
  The system checks key length before encryption/decryption to prevent misuse.

---

## ✅ Security Considerations & Limitations

* This project uses a **static key** for demonstration purposes.
* Uploads and decrypted files are stored locally — in real-world apps, this would be replaced by cloud storage with encryption at rest.
* No user authentication is implemented as it wasn’t required for this task scope.

---

## ✅ Recommendations for Production Use

* Implement user authentication and role-based access.
* Use HTTPS to secure file transfers.
* Implement file integrity checks using hashing (e.g., SHA-256).
* Rotate encryption keys periodically.

---

## 📌 Author Note

Prepared for educational and internship purposes only.
