from django.contrib import admin
from django.urls import path
from signup.views import signaction
from login.views import loginaction
from django.views.generic.base import RedirectView
from login.views import home_view 
from django.urls import path
# from videos.views import upload_video
import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('signup/', signaction, name='signup'),
    path('login/', loginaction, name='login'),
    path('home/', home_view, name='home'),
    path('', RedirectView.as_view(url='login/', permanent=True)),
    # path('upload/', upload_video, name='upload_video'),
    # path('upload/success/<int:video_id>/', views.upload_success, name='upload_success'),

]
