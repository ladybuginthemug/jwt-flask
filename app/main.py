from flask import Flask, request, jsonify
import jwt
from datetime import datetime, timedelta
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

app = Flask(__name__)

# Secret key for HS256
SECRET_KEY = 'your_super_secret_key'

# Load RSA keys (replace with your actual keys)
with open("rsa_private_key.pem", "rb") as priv_file:
    PRIVATE_KEY = serialization.load_pem_private_key(
        priv_file.read(),
        password=None,
        backend=default_backend()
    )

with open("rsa_public_key.pem", "rb") as pub_file:
    PUBLIC_KEY = serialization.load_pem_public_key(
        pub_file.read(),
        backend=default_backend()
    )


# Generate a JWT with HS256
@app.route('/generate-hs256', methods=['GET'])
def generate_hs256_token():
    payload = {
        'sub': 'user123',
        'role': 'user',
        'exp': datetime.utcnow() + timedelta(minutes=5)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return jsonify({'token': token})


# Generate a JWT with RS256
@app.route('/generate-rs256', methods=['GET'])
def generate_rs256_token():
    payload = {
        'sub': 'user123',
        'role': 'admin',
        'exp': datetime.utcnow() + timedelta(minutes=5)
    }
    token = jwt.encode(payload, PRIVATE_KEY, algorithm='RS256')
    return jsonify({'token': token})


# Verify a JWT token
@app.route('/verify', methods=['POST'])
def verify_token():
    token = request.json.get('token')
    try:
        # Attempt HS256 verification
        decoded_hs256 = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify({'decoded': decoded_hs256}), 200
    except jwt.exceptions.DecodeError:
        # Attempt RS256 verification
        try:
            decoded_rs256 = jwt.decode(token, PUBLIC_KEY, algorithms=['RS256'])
            return jsonify({'decoded': decoded_rs256}), 200
        except jwt.exceptions.InvalidSignatureError:
            return jsonify({'error': 'Invalid signature.'}), 401
        except jwt.exceptions.DecodeError:
            return jsonify({'error': 'Token cannot be decoded.'}), 401
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid Token'}), 401


if __name__ == '__main__':
    app.run(debug=True)
