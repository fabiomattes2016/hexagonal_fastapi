from pydantic import BaseModel


class BaseResponse(BaseModel):
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str