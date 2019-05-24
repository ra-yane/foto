from ..core import logger


class UsersError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        logger.critical('User error : {}'.format(message))

    def to_dict(self):
        return {'error': self.message}


class UserAlreadyRegistered(UsersError):
    def __init__(self):
        UsersError.__init__(self, 'This user is already registered.')


class UserNotExisting(UsersError):
    def __init__(self):
        UsersError.__init__(self, 'This user does not exist.')


class UserNotHelloFresh(UsersError):
    def __init__(self):
        UsersError.__init__(self, 'This user is not part of HelloFresh AU.', 401)


class BobLoginError(UsersError):
    def __init__(self):
        UsersError.__init__(self, 'Unable to connect to BOB.', 401)
