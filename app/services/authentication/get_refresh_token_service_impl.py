from app.services.ports.authenticationdataport import AuthenticationDataPort
from app.services.ports.authentication.get_refresh_token_service import GetRefreshTokenService


class GetRefreshTokenServiceImpl(GetRefreshTokenService):
    def __init__(self, authenticationport: AuthenticationDataPort) -> None:
        self.authenticationport = authenticationport


    async def get_refresh_token(self, token, db):
        return await self.authenticationport.get_refresh_token(token, db)
