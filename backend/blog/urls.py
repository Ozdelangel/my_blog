from django.urls import path
from django.urls.resolvers import URLPattern
from .views import PostList, PostDetail


urlpatterns = [
    path('', PostList.as_view(), name='List_view'),
    path('<int:pk>/', PostDetail.as_view(), name='Detail_view'),
    
]