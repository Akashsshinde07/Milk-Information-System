from django.contrib import admin
from django.urls import path
from . import views


#django admin header customization
admin.site.site_header = "Login To Developer Akash"
admin.site.site_title = "Welcome To Akash Dashboard"
admin.site.index_title = "Welcome To This Portal"

urlpatterns = [
    path("", views.index, name="index"),
    # User
    path("user_login/", views.user_login, name="user_login"),
    path("signup/", views.signup, name="signup"),
    path("user_homepage/", views.user_homepage, name="user_homepage"),
    path("logout/", views.Logout, name="logout"),

    path('about', views.about),

    path('base', views.base),
    path('cattle', views.cattle),
    path('gir cattle2', views.gir),
    path('demo', views.demo),
    path('deoni', views.deoni),
    path('result', views.result),
    path('deoni result', views.deoniresult),
    path('hariana cattle', views.hariana),
    path('hariana cattle result', views.harianaresult),
    path('krishna valley cattle', views.krishnavalley),
    path('krishna valley cattle result', views.krishnavalleyresult),
    path('murrah buffalo', views.murrah),
    path('murrah buffalo result', views.murrahresult),
    path('bhadawari buffalo', views.bhadawari),
    path('bhadawari buffalo result', views.bhadawariresult),
    path('pandharpuri buffalo', views.pandharpuri),
    path('pandharpuri buffalo result', views.pandharpuriresult),
    path('nagpuri buffalo', views.nagpuri),
    path('nagpuri buffalo result', views.result),
    path('add', views.add, name='add'),
    path('add1', views.add1, name='add1'),
    path('add2', views.add2, name='add2'),
    path('add3', views.add3, name='add3'),
    path('add4', views.add4, name='add4'),
    path('add5', views.add5, name='add5'),
    path('add6', views.add6, name='add6'),
    path('add7', views.add7, name='add7'),
]