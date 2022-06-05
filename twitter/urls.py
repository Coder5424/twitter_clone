from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='twitter/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('editor/', views.editor, name='editor'),
    path('follow/<str:username>', views.follow, name='follow'),
    path('unfollow/<str:username>', views.unfollow, name='unfollow'),
    path('search/', views.search, name='search'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)