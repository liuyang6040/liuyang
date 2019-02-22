from django.db import models

from utils.basemodel import BaseModel
class User(models.Model,BaseModel):
    apiid = models.CharField(max_length=100, verbose_name="接口ID")
    proid = models.CharField(max_length=100, verbose_name="项目id")
    ip = models.CharField(max_length=100, verbose_name="发送到的地址")
    port = models.CharField(max_length=100, verbose_name='端口号')
    mess = models.CharField(max_length=1000, verbose_name='信息')
    email = models.CharField(max_length=100, verbose_name='到邮箱')
    phonNo = models.CharField(max_length=100, verbose_name='到电话')
    apartment = models.CharField(max_length=100, verbose_name='所属部门')


    class Meta:
        db_table = "demo_api"
        verbose_name = "接口信息记录"