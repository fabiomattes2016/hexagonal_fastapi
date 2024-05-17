from app.services.ports.userdataport import UserDataPort
from app.domain.users.models import UserModel
from fastapi.exceptions import HTTPException
from app.infrastructure.security import get_password_hash


class UserDataAdapter(UserDataPort):
    async def save(self, data, db):
        user = db.query(UserModel).filter(UserModel.email == data.email).first()

        if user:
            raise HTTPException(status_code=302, detail="Email is already registered with us.")

        new_user = UserModel(
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email,
            password=get_password_hash(data.password),
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
