import unittest

from auth import Auth


class TestAuth(unittest.TestCase):
    def setUp(self):
        self._file_name = 'test_users.txt'

        self.auth = Auth(self._file_name)

        self._old_file_content = ''

        with open(self._file_name, 'r') as f:
            self._old_file_content = f.read()

    def tearDown(self):
        with open(self._file_name, 'w') as f:
            f.write(self._old_file_content)

    def test_has_user(self):
        result = self.auth.has_user('admin')
        self.assertTrue(result)
        result2 = self.auth.has_user('user')
        self.assertFalse(result2)

    def test_users_amount(self):
        self.assertEqual(self.auth.users_amount, 1)

    def test_validate_user(self):
        is_valid = self.auth.validate_user(name='admin', password='0000')
        self.assertTrue(is_valid)
        is_valid2 = self.auth.validate_user(name='admin', password='1111')
        self.assertFalse(is_valid2)
        is_valid3 = self.auth.validate_user(name='admin1', password='0000')
        self.assertFalse(is_valid3)

    def test_add_user(self):
        user_name = 'user'
        self.auth.add_user(name=user_name, password='1111')
        result = self.auth.has_user(user_name)
        self.assertTrue(result)
        self.assertEqual(self.auth.users_amount, 2)
    
    def test_delete_user(self):
        self.auth.delete_user(name='admin', password='0000')
        self.assertFalse(self.auth.has_user('admin'))
        self.assertEqual(self.auth.users_amount, 0)
        
if __name__ == '__main__':
    unittest.main()
