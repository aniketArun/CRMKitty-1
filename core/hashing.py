import bcrypt

class Hasher:
    @staticmethod
    def get_password_hashed(password: str) -> str:
        # Ensure password is bytes
        pw_bytes = password.encode("utf-8")

        # Option 1: Truncate if longer than 72 bytes
        if len(pw_bytes) > 72:
            pw_bytes = pw_bytes[:72]

        # Option 2 (better): Pre-hash with SHA256 to avoid silent truncation
        # pw_bytes = hashlib.sha256(pw_bytes).digest()

        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(pw_bytes, salt)
        return hashed.decode("utf-8")

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        pw_bytes = password.encode("utf-8")
        return bcrypt.checkpw(pw_bytes, hashed.encode("utf-8"))