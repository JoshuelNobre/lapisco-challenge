from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import delete, select
from src.schemas import User as SchemasUser
from src.models import User as ModelsUser
from sqlalchemy import update, delete


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: SchemasUser):
        db_user = ModelsUser(
            name=user.name,
            email=user.email,
            gender=user.gender,
            birth_data=user.birth_data,
            telephone=user.telephone,
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def list(self):
        users = self.db.query(ModelsUser).all()
        return users

    def list_by_id(self, id: int):
        consulta = select(ModelsUser).where(ModelsUser.id == id)
        list_user = self.db.execute(consulta).first()
        return list_user

    def edit(self, id: int, user: SchemasUser):
        updated_stmt = (
            update(ModelsUser)
            .where(ModelsUser.id == id)
            .values(name=user.name, telephone=user.telephone)
        )
        self.db.execute(updated_stmt)
        self.db.commit()

    def remove(self, id: int):
        delete_stmt = delete(ModelsUser).where(ModelsUser.id == id)
        self.db.execute(delete_stmt)
        self.db.commit()

    def get_by_email(self, email):
        query = select(ModelsUser).where(ModelsUser.email == email)
        return self.db.execute(query).scalars().first()
