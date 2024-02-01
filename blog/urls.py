from django.urls import path
from .views import PostsView, SinglePostView

urlpatterns=[
    path('', PostsView.as_view(), name='post_list'),
    path('<str:id>/<slug:slug>/', SinglePostView.as_view(), name='post_detail')
]