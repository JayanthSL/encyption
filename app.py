from flask import Flask, render_template, request, redirect, url_for, flash
import base64

app = Flask(__name__)
# app.secret_key = "your_secret_key"  # Required for flash messages


# Encryption function
def perform_encryption(message):
    encode_message = message.encode("ascii")
    base64_bytes = base64.b64encode(encode_message)
    return base64_bytes.decode("ascii")


# Decryption function
def perform_decryption(message):
    decode_message = message.encode("ascii")
    try:
        base64_bytes = base64.b64decode(decode_message)
        return base64_bytes.decode("ascii")
    except Exception as e:
        return f"Decryption failed: {str(e)}"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/encrypt", methods=["POST"])
def encrypt():
    password = request.form.get("code")
    message = request.form.get("text")

    if password == "123":
        if message.strip():
            encrypted_message = perform_encryption(message)
            return render_template(
                "result.html", result=encrypted_message, action="Encrypted"
            )
        else:
            flash("No text to encrypt", "error")
    elif password == "":
        flash("Please enter the secret key", "error")
    else:
        flash("Invalid secret key", "error")

    return redirect(url_for("index"))


@app.route("/decrypt", methods=["POST"])
def decrypt():
    password = request.form.get("code")
    message = request.form.get("text")

    if password == "1234":
        if message.strip():
            decrypted_message = perform_decryption(message)
            return render_template(
                "result.html", result=decrypted_message, action="Decrypted"
            )
        else:
            flash("No text to decrypt", "error")
    elif password == "":
        flash("Please enter the secret key", "error")
    else:
        flash("Invalid secret key", "error")

    return redirect(url_for("index"))


@app.route("/reset", methods=["POST"])
def reset():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
