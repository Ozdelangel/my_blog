from django.urls import path
from django.urls.resolvers import URLPattern
from .views import DeleteView,DetailView,CreateView,UpdateView,ListView


urlpatterns = [
    path('', ListView.as_view(), name='List_view'),
    path('<int:pk>', DetailView.as_view(), name='Detail_view'),
    path('', CreateView.as_view(), name='Create_view'),
    path('', UpdateView.as_view(), name='Update_view'),
    path('', DeleteView.as_view(), name='Delete_view')
]