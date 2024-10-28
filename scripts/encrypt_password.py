# source .venv/bin/activate && \
# pip install passlib
# (we should drop it tho, in app/ it requires us to use an outdated version of bcrypt as a dep.)

import argparse
from passlib.context import CryptContext

# Set up the bcrypt context
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_password(password: str) -> str:
    return bcrypt_context.hash(password)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hash a password for SQL INSERT.")
    parser.add_argument("password", help="Password to hash")
    
    args = parser.parse_args()
    hashed_password = hash_password(args.password)
    print(f"{args.password}: {hashed_password}")
