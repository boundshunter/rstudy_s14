from django.db import models

# Create your models here.

class UserInfo(models.Model):
    # id 默认创建列， 自增，主键
    # 字符串长度，指定类型
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
