from flask import Flask, render_template, request, send_from_directory, flash
import os
from encryption import encrypt_file, decrypt_file

app = Flask(__name__)
app.secret_key = 'supersecretkey'
UPLOAD_FOLDER = 'uploads'
DECRYPTED_FOLDER = 'decrypted'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file:
        data = uploaded_file.read()
        encrypted_data = encrypt_file(data)
        filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.filename + '.enc')
        with open(filepath, 'wb') as f:
            f.write(encrypted_data)
        flash('File uploaded and encrypted successfully!')
    return index()

@app.route('/download/<filename>')
def download_file(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    with open(filepath, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = decrypt_file(encrypted_data)

    decrypted_path = os.path.join(DECRYPTED_FOLDER, filename.replace('.enc', ''))
    with open(decrypted_path, 'wb') as f:
        f.write(decrypted_data)
    return send_from_directory(DECRYPTED_FOLDER, filename.replace('.enc', ''), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
