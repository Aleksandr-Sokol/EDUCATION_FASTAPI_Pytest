from .base import CRUDBase
from database.models import PersonData


class UserDataCRUD(CRUDBase):
    model = PersonData
