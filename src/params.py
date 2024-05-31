from auth import VerifyToken
from conf import UserType

auth_all = VerifyToken()
auth_staff = VerifyToken(UserType.staff_users())
