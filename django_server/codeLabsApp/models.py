from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(user, date):
        user = model(
            user=user,
            date=date
        )
        user.save(using=_db)
        return user

class MyUser(AbstractBaseUser):
    objects = MyUserManager()
    class Meta:
        # managed = False
        db_table = 'user_entity'

    user_id = models.AutoField(primary_key=True, db_column='userId')
    user = models.CharField(db_column='user', unique=True, max_length=20)
    date = models.DateTimeField(db_column='date', default=datetime.date.today)
    password = None
    last_login = None

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = ['date']

    def __str__(self):
        return str(self.user_id) + " (%s)" % str(self.user)
