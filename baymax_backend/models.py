from sqlalchemy import Column, Integer, String
from baymax_backend.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(300))
    last_name = Column(String(300))
    email = Column(String(300), unique=True)
    phone = Column(String(100))

    def __repr__(self):
        return '<User %r>' % (self.id)