from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from utils.basemodel import BaseModel
class User(AbstractUser, BaseModel):
    '''用户模型类'''
    phoneNo = models.CharField(max_length=12, verbose_name="电话号码")
    name = models.CharField(max_length=100, verbose_name="姓名")
    sex = models.CharField(max_length=10, verbose_name="性别")
    part=models.CharField(max_length=50,verbose_name='所属部门')

    class Meta:
        db_table = "demo_user"
        verbose_name = "用户表"