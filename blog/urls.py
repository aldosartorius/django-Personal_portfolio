
from django.urls import path
from blog import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.all_blogs, name = 'all_blogs'),
]
