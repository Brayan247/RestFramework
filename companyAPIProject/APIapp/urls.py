from django.urls import path
from .views import UserListView

urlpatterns = [
    path('user/', UserListView.as_view(), name='user_list')
]