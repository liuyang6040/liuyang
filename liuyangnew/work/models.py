from django.db import models
# Create your models here.
from utils.basemodel import BaseModel
class Project(models.Model, BaseModel):
    '''用户模型类'''
    title = models.CharField(max_length=100, verbose_name="项目名")
    userId = models.CharField(max_length=100, verbose_name="用户ID")
    ip= models.CharField(max_length=50, verbose_name="用户IP")
    port=models.CharField(max_length=100,verbose_name='端口号')
    dbType=models.CharField(max_length=100,verbose_name='业务类型')
    dbname=models.CharField(max_length=100,verbose_name='业务名字')
    acount=models.CharField(max_length=100,verbose_name='用户名')
    password=models.CharField(max_length=100,verbose_name='密码')
    sqlstat=models.CharField(max_length=1000,verbose_name='sql语句')
    status=models.CharField(max_length=100,verbose_name='是否开启')
    description=models.CharField(max_length=100,verbose_name='业务描述')

    class Meta:
        db_table = "demo_project"
        verbose_name = "项目表"
class Rule(models.Model, BaseModel):
    '''用户模型类'''
    title = models.CharField(max_length=100, verbose_name="监控名")
    ruleid=models.CharField(max_length=100, verbose_name="监控id")
    proId = models.CharField(max_length=100, verbose_name="项目id")
    level= models.CharField(max_length=50, verbose_name="水平")
    isSMS=models.CharField(max_length=100,verbose_name='用信息')
    isEmail=models.CharField(max_length=100,verbose_name='用邮箱')
    toUsers=models.CharField(max_length=100,verbose_name='发送给用户')
    status=models.CharField(max_length=100,verbose_name='')
    MinNum=models.CharField(max_length=100,verbose_name='最小值')
    MaxNum=models.CharField(max_length=1000,verbose_name='最大值')
    startTime=models.CharField(max_length=100,verbose_name='开启时间')
    endTime=models.CharField(max_length=100,verbose_name='结束时间')
    description=models.CharField(max_length=100,verbose_name='业务描述')

    class Meta:
        db_table = "demo_rule"
        verbose_name = "配置表"
class TheThird(models.Model, BaseModel):
    '''用户模型类'''
    endId = models.CharField(max_length=100, verbose_name="结果id")
    proId = models.CharField(max_length=100, verbose_name="项目id")
    endlevel= models.CharField(max_length=50, verbose_name="水平差")
    apartment=models.CharField(max_length=100,verbose_name='部门信息')
    endisEmail=models.CharField(max_length=100,verbose_name='用邮箱')
    MinNum=models.CharField(max_length=100,verbose_name='最小值')
    MaxNum=models.CharField(max_length=1000,verbose_name='最大值')
    startTime=models.CharField(max_length=100,verbose_name='开启时间')
    endTime=models.CharField(max_length=100,verbose_name='结束时间')
    description=models.CharField(max_length=100,verbose_name='业务描述')

    class Meta:
        db_table = "demo_end"
        verbose_name = "结果表"