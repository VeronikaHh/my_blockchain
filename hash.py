import hashlib


class Hash:
    @staticmethod
    def calculate(message: str) -> str:
        sha256_hash = hashlib.sha256()
        sha256_hash.update(message.encode('utf-8'))
        hashed_string = sha256_hash.hexdigest()
        return hashed_string
