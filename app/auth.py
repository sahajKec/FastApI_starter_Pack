from datetime import datetime, timedelta
from jose import jwt
import bcrypt
import hashlib
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

def hash_password(password: str) -> str:
    sha_password = hashlib.sha256(password.encode()).digest()
    hashed = bcrypt.hashpw(sha_password, bcrypt.gensalt())
    return hashed.decode('utf-8')


def verify_password(password: str, hashed: str) -> bool:
    sha_password = hashlib.sha256(password.encode()).digest()
    return bcrypt.checkpw(sha_password, hashed.encode('utf-8'))

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
