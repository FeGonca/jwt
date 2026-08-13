import jwt
from datetime import datetime, timezone, timedelta

class JwtHandler:
    def create_jwt_token(self, body: dict = {}) -> str:
        token = jwt.encode(
            payload={
                "exp": datetime.now(timezone.utc) + timedelta(minutes=5),
                **body
            },
            key="projetoJWT",
            algorithm="HS256"
        )
        return token

    def decode_jwt_token(self, token: str) -> dict:
        token_information = jwt.decode(token, key="projetoJWT", algorithms="HS256")
        return token_information