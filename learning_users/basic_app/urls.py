from django.urls import re_path
from basic_app import views
#template tagging
app_name = 'basic_app'

urlpatterns = [
    re_path('register/', views.register, name='register'),
    re_path('user_login',views.user_login,name='user_login')
]
