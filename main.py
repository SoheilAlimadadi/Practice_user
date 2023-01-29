from getpass import getpass

from user import (
    Username,
    Password
)

class Main:

    def run_program(self):
        username_valid = False
        password_valid = False
        while not username_valid:
            username = input('Username: ')
            username_valid = Username.check(username)

        while not password_valid:
            password = getpass('Password: ')
            password_valid = Password.check(password)

        print(username, password)








if __name__ == '__main__':
    main = Main()
    main.run_program()