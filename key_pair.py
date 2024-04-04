from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend


class KeyPair:
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate_key_pair():
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return KeyPair(public_key, private_key)
