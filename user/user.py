from .validators import (
    UsernameValidator,
    PasswordValidator
)

from helper.exceptions import(
    UsernameLengthError,
    UsernameStartDigitError,
    PasswordAlphabetError,
    PasswordDigitError,
    PasswordLowerCaseError,
    PasswordSignError,
    PasswordLengthError,
    PasswordUpperCaseError
)


class Username:
    @staticmethod
    def check(username):
        is_valid = False
        try:
            username = UsernameValidator(username)
        except UsernameLengthError as e:
            print(e)
        except UsernameStartDigitError as e:
            print(e)
        else:
            is_valid = True

        return is_valid


class Password:

    @staticmethod
    def check(password):
        is_valid = False
        try:
            password = PasswordValidator(password)
        except PasswordLengthError as e:
            print(e)
        except PasswordAlphabetError as e:
            print(e)
        except PasswordUpperCaseError as e:
            print(e)
        except PasswordLowerCaseError as e:
            print(e)
        except PasswordDigitError as e:
            print(e)
        except PasswordSignError as e:
            print(e)
        else:
            is_valid = True
        
        return is_valid