from django.conf.urls import url, include
from testapp import views

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
handlerw404 = "testapp.views.page_not_found"
handlerw500 = "testapp.views.page_error"
urlpatterns = [
    url(r'^index/', views.index),
    url(r'^cp_index/', views.cp_index),
    url(r'^login/', views.login),
    url(r'^test/', views.test),
    url(r'^cplogin/', views.cp_login),
    url(r'^register/', views.register),
    url(r'^change_o/(\w+)/$', views.Change_o),
    url(r'^c_change/$', views.C_change),
    url(r'^is_apply/(\w+)/',views.is_offer),
    url(r'^classes/(\w+)/', views.Classes),
    url(r'^mylove/(\w+)/', views.Mylove),
    url(r'^show_o/(\w+)/', views.show_o),
    url(r'^allinfo/(\w+)/', views.all_info),
    url(r'^mana/(\w+)/$', views.Info_mana),
    url(r'^add_say/$', views.add_say,name='add_say'),
    url(r'^add_info/(\w+)/$', views.addinfo),
    url(r'^cpregister/', views.cp_register),
    url(r'^logout/', views.logout),
    url(r'^del/(\d+)/', views.del_info),
    url(r'^fav/(\d+)/(\w+)/', views.Favorite),
    url(r'^apply/(\d+)/(\w+)/', views.apply),
    url(r'^details/(\d+)/(\w+)/', views.Showdetails, name='showd'),
    url(r'^search/(\d+)/$', views.Search),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
