from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, password=None, role=3):
        user = self.model(username=username)
        user.set_password(password)
        user.role = role
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.role = 1
        user.save(using=self._db)
        return user
