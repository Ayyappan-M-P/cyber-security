from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature
import os

def load_public_key(public_key_path):
    with open(public_key_path, 'rb') as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())
    return public_key

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False

def main(public_key_path, message_path, signature_path):
    # Load public key
    public_key = load_public_key(public_key_path)
    
    # Load message
    with open(message_path, 'rb') as msg_file:
        message = msg_file.read()
    
    # Load signature
    with open(signature_path, 'rb') as sig_file:
        signature = sig_file.read()
    
    # Verify the signature
    is_verified = verify_signature(public_key, message, signature)
    if is_verified:
        print("The signature is valid.")
    else:
        print("The signature is invalid or the message has been altered.")

if __name__ == "__main__":
    # Paths to the public key, message, and signature files
    public_key_path = "./public_key.pem"
    message_path = "./message.txt"
    signature_path = "./signature.sig"
    
    # Run the verification process
    main(public_key_path, message_path, signature_path)
