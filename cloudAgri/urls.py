from django.contrib import admin
from django.urls import path
from web import views
from web.scheduler import start
       
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('get',views.getdata,name='get'),
    path('on',views.seton),
    path('off',views.setoff),
    path('hardreload',views.update),
    path('pasttrend',views.past_trend,name='past_trend'),
]



