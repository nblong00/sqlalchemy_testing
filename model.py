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
        return f'<User(name = {self.name}, full_name = {self.full_name}, nickname = {self.nickname})'

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    new_users = [User(name='Grace', full_name='Grace Hopper', nickname='Pioneer'), User(name='Alan', full_name='Alan Turing', nickname='Computer Scientist'),  User(name='Katherine', full_name='Katherine Johnson', nickname='')]
    session.add_all(new_users)
    session.commit()

    for user in new_users:
        print(user.id)
