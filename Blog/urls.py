from django.urls import path
from . import views
from .views import PostListView, PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns= [
              path('' ,views.home, name = 'Blog-home'),
              path(' ', PostListView.as_view(), name='post-list' ),
              path('post/new/', PostCreateView.as_view(), name='post-create'),
              path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
              path('post/<int:pk>/Update', PostUpdateView.as_view(), name='post-update'),
              path('Post/<int:pk>/Delete', PostDeleteView.as_view(), name='post-delete'),
              
]