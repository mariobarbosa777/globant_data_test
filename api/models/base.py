from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True 

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
