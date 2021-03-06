import hashlib #import library for hashing
from typing import Optional, Tuple


class Auth: #class describing the user authorization
    def __init__(self, filename: str):
        self._filename = filename
        self._is_users_changed = False

        self._users = []

        with open(self._filename, 'r') as file_auth:
            for line in file_auth:
                name, pw_hash = line.split(',')
                self._users.append((name, pw_hash))

    @property
    def users_amount(self) -> int:
        return len(self._users)

    def has_user(self, username: str) -> bool:
        user = self._get_user(username)
        return user is not None

    def validate_user(self, name: str, password: str) -> bool:
        user = self._get_user(name)

        if user is not None:
            (username, pw_hash) = user
            _hash = hashlib.md5(password.encode()).hexdigest()
            return username == name and pw_hash == _hash
        else:
            return False

    def add_user(self, name: str, password: str): #adding a user
        pass_user = hashlib.md5(password.encode()).hexdigest()
        line = ','.join([name, pass_user])

        with open(self._filename, 'a') as file_auth:
            file_auth.write('\n' + line)

        self._users.append((name, pass_user))
    
    def delete_user(self, name: str, password: str):#delete a user
        for item in self._users:
            (username, _) = item

            if username == name:
                self._users.remove(item)
                break

    def _get_user(self, username: str) -> Optional[Tuple[str, str]]:
        for (name, pw_hash) in self._users:
            if name == username:
                return (name, pw_hash)
        
        return None
