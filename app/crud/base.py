from typing import TypeVar, Generic, Optional, Any, List
from app.sqlDB.base_class import Base
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: ModelType):
        self.model = model

    def get(
            self,
            db: Session,
            id: Any
    ) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_mulit(
            self,
            db: Session,
            skip: int,
            limit: int
    ) -> List[ModelType]:
        return db.query(self.model).limit(limit).offset(
            int(skip - 1) * limit
        ).all()

    def create(
            self,
            db: Session,
            obj_in: CreateSchemaType
    ) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        return db_obj

    def update(
            self,
            db: Session,
            db_obj: ModelType,
            obj_in: UpdateSchemaType
    ) -> ModelType:

        obj_data = jsonable_encoder(obj_in)
        if isinstance(db_obj, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        return db_obj

    def remove(
            self,
            db: Session,
            id: int
    ) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj



