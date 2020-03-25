from django.db import models
import django.utils.timezone as timezone
# Create your models here.
gender=(
    ('male','男'),
    ('female','女')
)
class_choice=(
    ('it','计算机'),
    ('service','服务业'),
    ('financial','金融'),
    ('realty','房地产'),
    ('medical','医疗'),
    ('education','教育'),
)
class User(models.Model):
    userid=models.AutoField(primary_key=True)
    user_name=models.CharField('账号',max_length=128)
    user_title=models.CharField('昵称',max_length=30)
    password=models.CharField('密码',max_length=256)
    createdate=models.DateTimeField('创建时间',auto_now_add=True,editable=True, null=True)
    user_email=models.EmailField('邮箱')
    user_sex=models.CharField('性别',max_length=20,choices=gender)
    user_tel=models.CharField('电话',max_length=20)
    address=models.CharField('地址',max_length=80)
    user_about=models.CharField('自我介绍',max_length=100)
    user_img=models.ImageField('头像',max_length=256,upload_to='img',default="img/default.png")
    #user_file=models.FileField('简历文件')
    class Meta:
        verbose_name = '用户'
        db_table='User'

class Company(models.Model):
    cp_id = models.AutoField(primary_key=True)
    cp_name = models.CharField('账号', max_length=128)
    cp_title = models.CharField('公司名', max_length=30)
    password = models.CharField('密码', max_length=256)
    createdate = models.DateTimeField('创建时间', auto_now_add=True,editable=True, null=True)
    cp_email = models.EmailField('邮箱')
    cp_tel = models.CharField('电话', max_length=20)
    cp_address = models.CharField('地址', max_length=80)
    cp_about = models.CharField('自我介绍', max_length=100)
    cp_img=models.ImageField('头像',max_length=256,upload_to='img',default="img/default.png")
    # user_file=models.FileField('介绍文件')
    class Meta:
        verbose_name = '公司'
        db_table='Company'
index_hot={
    ('yes', 'yes'),
    ('no', 'no'),
}

class Information(models.Model):
    info_id=models.AutoField(primary_key=True)
    cp_title=models.CharField('公司名', max_length=30)
    createdate=models.DateTimeField('发布时间',auto_now_add=True,editable=True, null=True)
    job=models.CharField('职位',max_length=20,default='')
    classes=models.CharField('类别',max_length=20,choices=class_choice)
    cp_email = models.EmailField('邮箱')
    pay=models.CharField('薪酬',max_length=50,default='3000-5000')
    cp_tel = models.CharField('电话', max_length=20)
    cp_address = models.CharField('地址', max_length=80)
    info=models.TextField('招聘内容')
    info_img=models.ImageField('图片',max_length=256,upload_to='img')
    views = models.PositiveIntegerField(default=0)
    is_hot=models.CharField('首页轮播',max_length=10,choices=index_hot,default='no')
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    class Meta:
        verbose_name = '招聘信息'
        db_table='Info'

class Comments(models.Model):
    com_id=models.AutoField(primary_key=True)
    info_id = models.CharField(max_length=256,default='')
    user_name = models.CharField(max_length=128, default='')
    user_title = models.CharField('昵称', max_length=30, default='')
    pay = models.CharField('薪酬', max_length=50, default='3000-5000')
    com_about=models.CharField('内容', max_length=30)
    com_time=models.DateTimeField('发布时间',auto_now_add=True,editable=True, null=True)

    class Meta:
        verbose_name = '评论'
        db_table='Com'
class Collection(models.Model):
    id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=128)
    info_id=models.CharField(max_length=256)
    pay = models.CharField('薪酬', max_length=50, default='3000-5000')
    cp_title = models.CharField('公司名', max_length=30, default='')
    job = models.CharField('职位', max_length=20, default='')
    col_time = models.DateTimeField('收藏时间', auto_now_add=True, editable=True, null=True)
    class Meta:
        verbose_name = '用户收藏'
        db_table='Col'

class C_collection(models.Model):
    id = models.AutoField(primary_key=True)
    user_title=models.CharField(max_length=30, default='')
    user_name = models.CharField(max_length=128, default='')
    cp_title=models.CharField(max_length=30, default='')
    job = models.CharField('职位', max_length=20, default='')
    info_id = models.CharField(max_length=256,default='')
    pay = models.CharField('薪酬', max_length=50, default='3000-5000')
    c_time = models.DateTimeField('投递时间', auto_now_add=True,editable=True, null=True)
    is_look=models.CharField('已查看',max_length=10,choices=index_hot,default='no')
    class Meta:
        verbose_name = '简历'
        db_table = 'C_col'
class Relationship(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ManyToManyField(User)
    com=models.ManyToManyField(Comments)
    company=models.ManyToManyField(Company)
    info=models.ManyToManyField(Information)
    col=models.ManyToManyField(Collection)
    class Meta:
        verbose_name = '关联'
        db_table='Relationship'