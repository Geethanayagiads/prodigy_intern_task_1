from flask import Flask, render_template, request

app = Flask(__name__)

def encrypt_text(plaintext, n):
    ans = ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch == " ":
            ans += " "
        elif ch.isupper():
            ans += chr((ord(ch) + n - 65) % 26 + 65)
        elif ch.islower():
            ans += chr((ord(ch) + n - 97) % 26 + 97)
        else:
            ans += ch
    return ans

def decrypt_text(ciphertext, n):
    ans = ""
    for i in range(len(ciphertext)):
        ch = ciphertext[i]
        if ch == " ":
            ans += " "
        elif ch.isupper():
            ans += chr((ord(ch) - n - 65) % 26 + 65)
        elif ch.islower():
            ans += chr((ord(ch) - n - 97) % 26 + 97)
        else:
            ans += ch
    return ans

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        operation = request.form['operation']
        if operation == 'encrypt':
            result = encrypt_text(text, shift)
        elif operation == 'decrypt':
            result = decrypt_text(text, shift)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
