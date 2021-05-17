"""createproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from projectPage01 import views as page01_views
from testMySQL import views as mysql_views
import re
urlpatterns = [
    path('admin/', admin.site.urls),
    #驗證配置
    #path('', page01_views.defaultHomePage),
    path('test.html/', page01_views.testdefault),

    path('user/',page01_views.setui),
    path('user/',include(
        [
            path('welcome.html/',page01_views.welcomePage),
        ]
    )),
    # path(r'buttonPage/search/', views.searchPage),
    # path(r'buttonPage/update/', views.updatePage),
    # path(r'buttonPage/add/', views.addPage),
    path('buttonPage/', page01_views.buttonPage),
    #定義公用路徑
    path('buttonPage/', include(
            [path('search/', page01_views.functionSearch),
             path('update/', page01_views.updatePage),
             path('add/', page01_views.addPage),

            ]
        )
    ),
    #?name=dsd&num_area=20&address=sds&tel1=sds&tel2=sdsd&note=sdsd

    #re_path('restadd/<str>', views.functionAdd),
    re_path('^restadd/$',page01_views.functionAdd),
    #=============================================================================================
    #=============================================================================================
    #=============================================================================================
    #factory
    path('', mysql_views.defaultHomePage),
    path('test.html/', mysql_views.testdefault),

    path('factoryUser/', mysql_views.setui),
    path('factoryUser/', include(
        [
            path('welcome.html/', mysql_views.welcomePage),
        ]
    )),
    # path(r'buttonPage/search/', views.searchPage),
    # path(r'buttonPage/update/', views.updatePage),
    # path(r'buttonPage/add/', views.addPage),
    path('factory/', mysql_views.buttonPage),
    # 定義公用路徑
    path('factory/', include(
        [
            path('search/', mysql_views.functionSearch),
            path('update/', mysql_views.updatePage),
            path('add/', mysql_views.addPage),
            #path('ddropTable',mysql_views.dropTable),
            path('search_c/',mysql_views.search_condition),
            re_path('^search_c/?P<str:name>/$',mysql_views.search_coditioin_name),
         ]
    )
         ),
    # ?name=dsd&num_area=20&address=sds&tel1=sds&tel2=sdsd&note=sdsd

    # re_path('restadd/<str>', views.functionAdd),
    re_path('^factoryrestadd/$', mysql_views.functionAdd),



]

"""
path('<page_slug>-<page_id>/', include([
        path('history/', views.history),
        path('edit/', views.edit),
        path('discuss/', views.discuss),
        path('permissions/', views.permissions),
    ])),

"""
