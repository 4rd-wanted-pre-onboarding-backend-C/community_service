from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, account_name, gender, age, password=None):
        if not account_name:
            raise ValueError("계정 이름을 입력해주세요.")
        if not gender:
            raise ValueError("성별을 입력해주세요.")
        if not age:
            raise ValueError("나이를 입력해주세요.")

        user = self.model(
            account_name = account_name,
            gender = gender,
            age = age,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, account_name, password=None):
        user = self.create_user(
            account_name = account_name,
            password = password,
            name = name
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    account_name = models.CharField(verbose_name="ID", max_length=15, unique=True)
    user_name = models.CharField(verbose_name="이름", max_length=20)
    gender = models.BooleanField(verbose_name="성별")
    age = models.IntegerField(verbose_name="나이")
    phone = models.CharField(verbose_name="휴대폰 번호", max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    teamgruop_id = models.ForeignKey("TeamGruop", on_delete=models.CASCADE)

    # status
    is_staff = models.BooleanField()
    is_active = models.BooleanField()

    USERNAME_FIELD = "account_name"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"


class TeamGroup(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "teams_groups"


class History(models.Model):
    last_login = models.DateTimeField(null=True) # 로그인 시 view에서 구현 예정
    last_logout = models.DateTimeField(null=True) # 로그아웃 시 view에서 구현 예정
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)

    class Meta:
        db_table = "histories"