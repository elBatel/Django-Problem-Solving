from django.shortcuts import render
from .models import UserInfo
from .filters import UserTypeFilter

def list_user(request):
    users   = UserInfo.objects.all()
    user_filter = UserTypeFilter(request.GET, queryset=users)
    context = { 
        'users': users ,
        'filter': user_filter,
    }
    return render(request, 'choices_test/list_user.html', context) 


