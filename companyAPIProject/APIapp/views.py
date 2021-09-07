from django.views import View
from .models import User
from django.http import JsonResponse

class UserListView(View) :
    def get(self, request) :
        ulist = User.objects.all()
        return JsonResponse(list(ulist.values()), safe =False)

class UserDetailView(View) :
    def get(self, request, pk) :
        ulist = User.objects.get(pk = pk)
        return JsonResponse(ulist)
