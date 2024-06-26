from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post,UserInfo, Tag,Comment,React,HistoryChat
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'star', 'address','slug')
    ordering = ('id',)
admin.site.register(Post,PostAdmin)
class UserInfoAdmin(admin.ModelAdmin):
    list_display=('id','firstname','lastname','phonenumber','gender', 'date')
    ordering = ('id',)
admin.site.register(UserInfo,UserInfoAdmin)
admin.site.unregister(User)  # Hủy đăng ký mô hình người dùng mặc định
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff')
    ordering = ('id',)
admin.site.register(User, CustomUserAdmin)  # Đăng ký mô hình người dùng với cấu hình tùy chỉnh

admin.site.register(Tag)

class CustomComment(admin.ModelAdmin):
    list_display=('id','content','date')
    ordering = ('id',)
admin.site.register(Comment,CustomComment) 

class CustomReact(admin.ModelAdmin):
    list_display=('id','star','idpost','iduser')
    ordering = ('id',)
    
admin.site.register(React,CustomReact)

admin.site.register(HistoryChat)