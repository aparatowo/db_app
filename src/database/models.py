from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Image(Base):
    __tablename__ = "Images"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    link = Column(String(), nullable=False)


