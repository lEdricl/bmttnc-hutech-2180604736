from flask import jsonify, request
from flask import Flask, request

from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)



#RAILFENCE CIPHER
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt',methods=['POST'])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypt_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypt_text': encrypt_text})

@app.route('/api/railfence/decrypt',methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypt_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypt_text': decrypt_text})

playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods = ['POST'])
def playfair_creatematrix():
    data = request.json
    key = data ['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route('/api/playfair/encrypt', methods = ['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods = ['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text':decrypted_text})



#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)