from sqlalchemy import Column, Integer, String

from db import Base, engine, db_session


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(15), nullable=False)
    email = Column(String(50), nullable=False)


if __name__ == "__main__":
    Base.metadata.create_all(engine)


