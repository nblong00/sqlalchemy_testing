from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db', echo = False)
Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    full_name = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'<User(name = {self.name}, full_name = {self.full_name}, nickname = {self.nickname})>'

if __name__ == '__main__':
    Base.metadata.create_all(engine)
