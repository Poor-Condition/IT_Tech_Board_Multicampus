from django.contrib import admin

# admin 페이지에서 Like도 관리 할 수 있도록 등록시키시오
# Register your models here.
from django.contrib import admin
from .models import User,Like

admin.site.register(User)
admin.site.register(Like)