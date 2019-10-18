import django_filters
from .models import UserInfo

class UserTypeFilter(django_filters.FilterSet):
    class Meta:
        model = UserInfo
        fields = ['user_type']