from app.services.ports.authenticationdataport import AuthenticationDataPort
from app.services.ports.authentication.verify_token_service import VerifyTokenService

class VerifyTokenServiceImpl(VerifyTokenService):
    def __init__(self, authenticationport: AuthenticationDataPort) -> None:
        self.authenticationport = authenticationport


    async def verify_token(self, token, db):
        return await self.authenticationport.verify_token(token, db)
