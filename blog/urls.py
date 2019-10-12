from .views import PostList, PostDetail, Policy
from django.urls import path

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('policy/', Policy.as_view(), name='policy'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
