from app.services.ports.authenticationdataport import AuthenticationDataPort
from app.services.ports.authentication.get_token_service import GetTokenService


class GetTokenServiceImpl(GetTokenService):
    def __init__(self, authenticationport: AuthenticationDataPort) -> None:
        self.authenticationport = authenticationport


    async def get_token(self, data, db):
        return await self.authenticationport.get_token(data, db)
