from django.urls import path
from blog import views
import blog.views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView


urlpatterns = [
    path('index/',views.index, name="index"),
    path('New/', HomeView.as_view(), name='New'),
    path('CreatePost/', AddPostView.as_view(), name='CreatePost'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='Detail'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
]