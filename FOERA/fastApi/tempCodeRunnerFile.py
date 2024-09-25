def create_access_token(data: dict, expires_delta: timedelta = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=30)  # Default to 30 min if not specified
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

# def decode_access_token(token: str):
#     try:
#         decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return decoded_data if decoded_data.get("exp") > datetime.utcnow().timestamp() else None
#     except jwt.PyJWTError:
#         return None