from conf import UserType
from dependencies.auth import VerifyToken

auth_all = VerifyToken()
auth_staff = VerifyToken(UserType.staff_users())

SUB_PATH = {
    "author": "/authors/",
    "book": "/books/",
    "topic": "/topics/",
    "post": "/posts/",
}
