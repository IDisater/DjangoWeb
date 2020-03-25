from django.forms import ModelForm, ValidationError
from testapp.models import User, Company, Information, Relationship,C_collection,Comments
from django import forms



'''class UserForm(ModelForm):
    captcha = CaptchaField(label='验证码')
    class Meta:
        model = User
        fields = '__all__'


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class InformationForm(ModelForm):
    class Meta:
        model = Information
        fields = '__all__'


class RelationshipForm(ModelForm):
    class Meta:
        model = Relationship
        fields = '__all__'
'''




class UserForm(forms.Form):
    user_name=forms.CharField(label='用户名',max_length=128,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(label='密码',max_length=256,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    user_name = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_title=forms.CharField(label='昵称', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    user_email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    user_sex = forms.ChoiceField(label='性别', choices=gender)

class InformationForm(forms.Form):
    class_choice = (
        ('it', '计算机'),
        ('service', '服务业'),
        ('financial', '金融'),
        ('realty', '房地产'),
        ('medical', '医疗'),
        ('education', '教育'),
    )
    job=forms.CharField(label='职位',max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    classes = forms.ChoiceField(label='岗位类别', choices=class_choice)
    cp_title = forms.CharField(label='公司名称', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pay = forms.CharField(label='薪酬', max_length=50)
    cp_email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    cp_address = forms.CharField(label='公司地址', max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cp_tel = forms.CharField(label='公司电话', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    info=forms.CharField(label='岗位描述', max_length=256, widget=forms.TextInput(attrs={'class': '🔠input1'}))
    info_img=forms.ImageField(label='宣传图')

class UserForm1(forms.Form):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    user_title=forms.CharField(label='昵称', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    user_sex = forms.ChoiceField(label='性别', choices=gender)
    user_tel = forms.CharField(label='电话', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='地址', max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_about = forms.CharField(label='自我介绍', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #user_img = forms.ImageField(label='头像')

class CpForm(forms.Form):
    cp_name=forms.CharField(label='用户名',max_length=128,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(label='密码',max_length=256,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class CompanyForm(forms.Form):
    cp_name = forms.CharField(label='账户', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cp_title = forms.CharField(label='公司名称', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    cp_email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    cp_address=forms.CharField(label='公司地址',max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cp_tel=forms.CharField(label='公司电话',max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cp_about=forms.CharField(label='公司介绍',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cp_img = forms.ImageField(label='头像')

class CompanyForm1(forms.Form):
    cp_title = forms.CharField(label='公司名称', max_length=128,widget=forms.TextInput(attrs={'class': 'form-control'}))
    cp_email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    cp_address = forms.CharField(label='公司地址', max_length=80,widget=forms.TextInput(attrs={'class': 'form-control'}))
    cp_tel = forms.CharField(label='公司电话', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cp_about = forms.CharField(label='公司介绍', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
        #cp_img = forms.ImageField(label='头像')
class C_collectionForm(ModelForm):
    class Meta:
        model = C_collection
        fields = '__all__'
class ComForm(ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'