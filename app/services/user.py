import uuid

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.errors import APIException
from app.models import query_session, action_session
from app.models.base import db
from app.models.user import Users
from app.services import BaseService


class UsersService(BaseService):
    def __init__(self):
        super(UsersService, self).__init__(model=Users, name="Users Service")

    def create_client(self, query_args=None):
        query_args = dict((key, value) for key, value in query_args.items() if value != '')
        self.register_user_by_account(query_args)
        return Success()

    def register_user_by_account(self, data=None):
        user = Users.query.filter_by(name=data['name']).all()
        if user:
            raise APIException()

        with action_session() as session:
            user = Users()
            user.name = data['name']
            user.uuid = uuid.uuid4().hex
            session.add(user)
        user = Users.query.filter_by(name=data['name']).first_or_404()
        print(user)

    def register_user_by_phone(self):
        print("111111")
        pass

    def register_user_by_email(self):
        print("11111")
        pass


if __name__ == '__main__':
    data={
        'name':'admin',
        'pwd':'ace123'
    }
    user = UsersService()
    user.register_user_by_account(data)
    # user.create_client()
