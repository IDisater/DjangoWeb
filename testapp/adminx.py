# xadmin全局配置
import xadmin
from xadmin import views
from . import models
class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "网上人才招聘系统后台管理"  # 设置站点标题
    site_footer = "刘洋洋"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠

xadmin.site.register(views.CommAdminView, GlobalSettings)
class EmailVerifyRecordAdmin(object):
    search_fields = ['code','email','send_type']
# 注册
xadmin.site.register(models.User)
xadmin.site.register(models.Information)
xadmin.site.register(models.Collection)
xadmin.site.register(models.Comments)
xadmin.site.register(models.C_collection)
xadmin.site.register(models.Company)
xadmin.site.register(models.Relationship)