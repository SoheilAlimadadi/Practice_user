from enum import StrEnum


class UserErrorMessages(StrEnum):
    USERNAME_LENGTH = "Username must be atleast 4 characters"
    USERNAME_AlPHA = "Username must start with an alphabet character"
    PASSWORD_LENGTH = "Password must be atleast 8 characters"
    PASSWORD_ALPHA = "Password must have atleast 2 alphabetic characters"
    PASSWORD_UPPER = "Password must have atleast 1 uppercase letter"
    PASSWORD_LOWER = "Password must have atleast 1 lowercase letter"
    PASSWORD_SIGN = "Password must have atleast one sign character"
    PASSWORD_DIGIT = "Password must have atleast one digit"
 