from datetime import datetime
from django.db import models
from django_gravatar.helpers import get_gravatar_url

class User(models.Model):
    """用户表"""
    username = models.CharField(verbose_name="用户名", max_length=32, unique=True, null=False)
    password = models.CharField(verbose_name="密码", max_length=128, null=False)
    avatar = models.CharField(verbose_name="用户头像", max_length=128)

    def save(self, *args, **kwargs):
        """生成用户头像"""
        self.avatar = get_gravatar_url(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return '<User %r>' % self.username

# Create your models here.
class Rsa(models.Model):
    """私钥"""
    status_choices = (
        (1, "启用"),
        (2, "停用"),
    )
    status =models.PositiveIntegerField(verbose_name="状态", choices=status_choices)
    user =models.CharField(verbose_name="用户", max_length=32, default="root")
    name = models.CharField(verbose_name="密钥名称", max_length=32)
    private_key =models.TextField(verbose_name="私钥")
    create_time = models.DateTimeField(verbose_name="创建时间", default=datetime.now)

