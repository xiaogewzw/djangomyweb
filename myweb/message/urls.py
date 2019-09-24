from django.urls import path
from . import views

app_name = 'message'
urlpatterns =[
    path('' , views.index , name = 'index'),
    path('messagedetail/<int:message_id>/' , views.messagedetail , name = 'messagedetail'),
    path('login/' , views.login , name = 'login'),
    path('register/' , views.register , name = 'register'),
    path('userinterface/' , views.userinterface , name = 'userinterface'),
]  