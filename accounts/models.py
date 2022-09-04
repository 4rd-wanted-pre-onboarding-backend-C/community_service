from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, gender, age, teamgroup_id, password=None):
        if not username:
            raise ValueError("계정 이름을 입력해주세요.")
        if not password:
            raise ValueError("비밀번호를 입력해주세요.")
        if not gender:
            raise ValueError("성별을 입력해주세요.")
        if not age:
            raise ValueError("나이를 입력해주세요.")

        user = self.model(
            username = username,
            password = password,
            gender = gender,
            age = age,
            teamgroup_id = TeamGroup.objects.get(id=teamgroup_id).id
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, gender, age, teamgroup_id, password=None):
        user = self.create_user(
            username = username,
            password = password,
            gender = gender,
            age = age,
            teamgroup_id = TeamGroup.objects.get(id=teamgroup_id).id
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class TeamGroup(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "teams_groups"


class User(AbstractUser):
    username = models.CharField(verbose_name="ID", max_length=20, unique=True)
    name = models.CharField(verbose_name="이름", max_length=15)
    gender = models.BooleanField(verbose_name="성별", default=True)
    age = models.IntegerField(verbose_name="나이")
    phone = models.CharField(verbose_name="휴대폰 번호", max_length=15, unique=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    teamgroup = models.ForeignKey("TeamGroup", on_delete=models.CASCADE)

    # status
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # except
    first_name = None
    last_name = None
    email = None

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["gender", "age", "teamgroup_id"]

    class Meta:
        db_table = "users"