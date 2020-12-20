from flask import Flask, render_template, request, jsonify, abort
from crypto_package import CaesarCipher, Des, Aes, DiffieHellman, MonoAlphabetCipher, \
    RailFence, SimpleColumnarTransposition, VernamCipher

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/cipher/caesar/")
def caesar_cipher_front():
    return render_template("caesar.html")


@app.route("/cipher/mono/")
def mono_cipher_front():
    return render_template("mono.html")


@app.route("/cipher/rail/")
def rail_cipher_front():
    return render_template("rail.html")


@app.route("/cipher/columnar/")
def columnar_cipher_front():
    return render_template("columnar.html")


@app.route("/cipher/vernam/")
def vernam_cipher_front():
    return render_template("vernam.html")


@app.route("/cipher/hellman/")
def hellman_cipher_front():
    return render_template("hellman.html")


@app.route("/crypto/aes/")
def aes_cipher_front():
    return render_template("aes.html")


@app.route("/crypto/des/")
def des_cipher_front():
    return render_template("des.html")


@app.route("/api/cipher/caesar/", methods=["POST"])
def caesar_cipher_back():
    data = request.get_json(force=True)
    operation = data["type"]
    text = data["text"]
    key = int(data["key"])
    if operation == "encrypt":
        cipher_text = CaesarCipher.encrypt(key, text)
        return jsonify({"output": cipher_text})
    else:
        cipher_text = CaesarCipher.decrypt(key, text)
        return jsonify({"output": cipher_text})


@app.route("/api/cipher/mono/", methods=["POST"])
def mono_cipher_back():
    data = request.get_json(force=True)
    operation = data["type"]
    text = data["text"]
    plain = data["plain"]
    sub = data["sub"]
    sub_table = {}
    for p, s in zip(plain, sub):
        sub_table[p] = s
    if operation == "encrypt":
        cipher_text = MonoAlphabetCipher.encrypt(sub_table, text)
        return jsonify({"output": cipher_text})
    else:
        cipher_text = MonoAlphabetCipher.decrypt(sub_table, text)
        return jsonify({"output": cipher_text})


@app.route("/api/cipher/rail/", methods=["POST"])
def rail_cipher_back():
    data = request.get_json(force=True)
    operation = data["type"]
    text = data["text"]
    key = int(data["key"])
    if operation == "encrypt":
        cipher_text = RailFence.encrypt(text, key)
        return jsonify({"output": cipher_text})
    else:
        cipher_text = RailFence.decrypt(text, key)
        return jsonify({"output": cipher_text})


@app.route("/api/cipher/columnar/", methods=["POST"])
def columnar_cipher_back():
    data = request.get_json(force=True)
    operation = data["type"]
    text = data["text"]
    key = int(data["key"])
    if operation == "encrypt":
        cipher_text = SimpleColumnarTransposition.encrypt(text, key)
        return jsonify({"output": cipher_text})
    else:
        cipher_text = SimpleColumnarTransposition.decrypt(text, key)
        return jsonify({"output": cipher_text})


@app.route("/api/cipher/vernam/", methods=["POST"])
def vernam_cipher_back():
    data = request.get_json(force=True)
    operation = data["type"]
    text = data["text"]
    key = data["key"]
    if len(text) != len(key):
        return abort(400)
    if operation == "encrypt":
        cipher_text = VernamCipher.encrypt(key, text)
        return jsonify({"output": cipher_text})
    else:
        cipher_text = VernamCipher.decrypt(key, text)
        return jsonify({"output": cipher_text})


@app.route("/api/cipher/hellman/", methods=["POST"])
def hellman_cipher_back():
    data = request.get_json(force=True)
    n = int(data["n"])
    g = int(data["g"])
    messages = []
    key, a, b, x, y = DiffieHellman.calculate_key(n, g)
    messages.append(f"Alice and Bob agreed on the numbers {n} and {g}.")
    messages.append(f"Alice choose another large random number x ({x}) and calculates A ({a}).")
    messages.append(f"A = {g}^{x} mod {n}")
    messages.append("Alice sent the number (A) calculated to Bob.")
    messages.append(f"Bob independently choose another large random number y ({y}) and calculates B ({b}).")
    messages.append(f"B = {g}^{y} mod {n}")
    messages.append("Bob sent the number (B) calculated to Alice")
    messages.append("Bob and Alice now calculate the key.")
    messages.append(f"Key = {key}")
    return jsonify({"output": messages})


@app.route("/api/crypto/aes/", methods=["POST"])
def aes_cipher_back():
    data = request.get_json(force=True)
    operation = data["type"]
    text: str = data["text"]
    key: str = data["key"]
    mode = data["mode"]
    if operation == "encrypt":
        cipher_text = Aes.encrypt(key.encode("utf-8"), text.encode("utf-8"), mode)
        return jsonify({"output": cipher_text})
    else:
        cipher_text = Aes.decrypt(key.encode("utf-8"), text, mode)
        return jsonify({"output": cipher_text})


@app.route("/api/crypto/des/", methods=["POST"])
def des_cipher_back():
    data = request.get_json(force=True)
    operation = data["type"]
    text: str = data["text"]
    key: str = data["key"]
    mode = data["mode"]
    if operation == "encrypt":
        cipher_text = Des.encrypt(key.encode("utf-8"), text.encode("utf-8"), mode)
        return jsonify({"output": cipher_text})
    else:
        cipher_text = Des.decrypt(key.encode("utf-8"), text, mode)
        return jsonify({"output": cipher_text})


if __name__ == "__main__":
    app.run()
