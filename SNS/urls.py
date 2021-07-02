from django.contrib import admin
from django.urls import path, include
from . import views
import home.urls

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include(home.urls))
   # path('', views.index, name='Home'),
   # path('SignIn', views.SignIn, name='SignUp')
]