from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error_code import ServerError
from app.libs.errors import APIException

app = create_app()

# @app.errorhandler(Exception)
# def framework_error(e):
#     if isinstance(e, APIException):
#         return e
#     if isinstance(e, HTTPException):
#         code = e.code
#         msg = e.description
#         error_code = 1007
#         return APIException(msg, code, error_code)
#     else:
#         # TODO log
#         if not app.config['DEBUG']:
#             return ServerError()
#         else:
#             raise e


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=8520, debug=True)
    app.run(host="0.0.0.0", port=8520, debug=True)
