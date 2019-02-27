from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey, orm
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import AuthFailed
from app.models.base import Base, db


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), unique=True)
    avatar_url = Column(String(128), comment='头像')
    phone = Column(String(11), unique=True)
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符

    user_auths = relationship('UserAuth', back_populates="users")

    def __repr__(self):
        return '<Users: {},{}>'.format(self.id, self.name)


class UserAuth(Base):
    __tablename__ = 'user_auths'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    identity_type = Column(String(64), comment='登陆方式')
    identifier = Column(String(64), comment='账号标识')
    credential = Column(String(64), comment='凭证')

    users = relationship('Users', back_populates="user_auths")

    def __repr__(self):
        return '<UserAuth: {},{},{},{},{}>'.format(
            self.id,
            self.user_id,
            self.identity_type,
            self.identifier,
            self.credential
        )

# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     nickname = Column(String(24))
#     email = Column(String(50))
#     phone = Column(String(11))
#     _password = Column('password', String(128))
#     role = Column(String(64))
#     memo = Column(String(128), nullable=True)
#     headimg = Column(String(256))
#     last_time = Column(Integer)
#     last_ip = Column(String(16))
#
#     @orm.reconstructor
#     def __init__(self):
#         self.fields = ['id', 'email', 'nickname']
#
#     def keys(self):
#         return self.fields
#
#     def hide(self, *keys):
#         [self.fields.remove(key) for key in keys]
#
#     def append(self, *keys):
#         [self.fields.append(key) for key in keys]
#
#     @property
#     def password(self):
#         return self._password
#
#     @password.setter
#     def password(self, raw):
#         self._password = generate_password_hash(raw)
#
#     @staticmethod
#     def register_by_email(nikename, account, secert):
#         with db.auto_commit():
#             user = User()
#             user.nickname = nikename
#             user.email = account
#             user.password = secert
#             db.session.add(user)
#
#     @staticmethod
#     def verify(email, password):
#         user = User.query.filter_by(email=email).first_or_404()
#         if not user.check_password(password):
#             raise AuthFailed()
#         scope = 'SuperScope' if user.auth == 2 else 'UserScope'
#         return {'uid': user.id, 'scope': scope}
#
#     def check_password(self, raw):
#         if not self._password:
#             return False
#         return check_password_hash(self._password, raw)
