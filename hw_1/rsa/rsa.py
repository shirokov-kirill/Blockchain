import hashlib
import rsa

class RSA_algorithm:

    def __init__(self):
        pass

    def generate_Pk_and_pk(self, p, q):
        pk, Pk = rsa.generate_Pk_and_pk(p, q)
        return Pk, pk

    def sign_string(self, text, pk):
        h = hashlib.new('sha512_256')
        h.update(text.encode())
        return rsa.encrypt_string(h.hexdigest(), pk)

    def verify_signature(self, signed_str, text, Pk):
        h_a = rsa.decrypt_string(signed_str, Pk)
        h_b = hashlib.new('sha512_256')
        h_b.update(text.encode())
        if h_a == h_b.hexdigest():
            return True
        else:
            return False

