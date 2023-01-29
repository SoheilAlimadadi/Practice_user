from .enums import UserErrorMessages as UEM


class UsernameLengthError(ValueError):
    
    def __str__(self):
        return UEM.USERNAME_LENGTH


class UsernameStartDigitError(ValueError):

    def __str__(self):
        return UEM.USERNAME_AlPHA


class PasswordLengthError(ValueError):

    def __str__(self):
        return UEM.PASSWORD_LENGTH


class PasswordAlphabetError(ValueError):

    def __str__(self):
        return UEM.PASSWORD_ALPHA


class PasswordUpperCaseError(ValueError):

    def __str__(self):
        return UEM.PASSWORD_UPPER


class PasswordLowerCaseError(ValueError):

    def __str__(self):
        return UEM.PASSWORD_LOWER


class PasswordSignError(ValueError):

    def __str__(self):
        return UEM.PASSWORD_SIGN


class PasswordDigitError(ValueError):

    def __str__(self):
        return UEM.PASSWORD_DIGIT
