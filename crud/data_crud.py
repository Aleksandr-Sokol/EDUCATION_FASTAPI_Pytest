from .base import CRUDBase
from database.models import UserData


class UserDataCRUD(CRUDBase):
    model = UserData
