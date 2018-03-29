from django.db import models

# Create your models here.

sex_list = (
     (0, '男'),
     (1, '女'),

)


class Profile(models.Model):
    nickname = models.CharField(max_length=128,verbose_name='昵称',null=True,blank=True)
    address = models.TextField(verbose_name='住址',null=True,blank=True)
    sex = models.IntegerField(choices=sex_list,null=True,blank=True)
    paymentpassword = models.CharField(max_length=256,verbose_name='支付密码',null=True,blank=True)
    avatar = models.ImageField(upload_to='upload/avatar/%Y/%m/%d',verbose_name='头像',null=True,blank=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='更新时间')
    class Meta:

        verbose_name = '用户资料'

    def __str__(self):
        return self.nickname

auth_type_list = (
    ('username', '用户密码认证'),
    ('email', '邮箱认证'),
    ('phone', '手机号认证'),
    # ('weibo','微博认证'),
    # ('wexin','微信认证'),
    # ('mi','小米认证')
)

class Auth(models.Model):
    profile = models.ForeignKey(Profile,verbose_name='认证用户',on_delete=models.CASCADE,null=True,blank=True)
    auth_type = models.CharField(choices=auth_type_list,verbose_name='认证类型',null=True,blank=True,max_length=256)
    token = models.CharField(max_length=256,verbose_name='密码或者令牌',null=True,blank=True)
    checked = models.BooleanField(default=False,verbose_name='是否认证过')
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='更新时间')

    class Meta:

        verbose_name = '用户认证'

    def __str__(self):
        return self.profile.nickname + '/' + self.auth_type

class DemandType(models.Model):
    name = models.CharField(max_length=256,verbose_name='需求类型',null=True,blank=True)

    class Meta:

        verbose_name = '需求类型'

    def __str__(self):
        return self.name

class Demand(models.Model):
    type = models.ForeignKey(DemandType,verbose_name='需求类型',null=True,blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=128,verbose_name='需求标题',null=True,blank=True)
    content = models.TextField(null=True,blank=True,verbose_name='需求说明')
    dead_line = models.DateTimeField(verbose_name='截至时间',null=True,blank=True)
    attachment = models.FileField(upload_to='upload/attachment/%Y/%m/%d',verbose_name='附件',null=True,blank=True)
    budget = models.IntegerField(null=True,blank=True,verbose_name='预算')
    user = models.ForeignKey(Profile,null=True,blank=True,verbose_name='发布者',on_delete=models.CASCADE)

    class Meta:
        verbose_name = '需求'

    def __str__(self):
        return self.title

