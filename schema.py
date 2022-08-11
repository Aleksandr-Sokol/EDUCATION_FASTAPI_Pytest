from pydantic import BaseModel


class PersonDataSchema(BaseModel):
    name: str
    family: str
    age: int

    class Config:
        orm_mode = True


class PersonDataDataSchema(PersonDataSchema):
    id: int


class UserSchema(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True


class UserDataSchema(UserSchema):
    id: int
