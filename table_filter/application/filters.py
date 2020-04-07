from django.contrib.auth.models import User
import django_filters

class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    username = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    year_joined = django_filters.NumberFilter(field_name='date_joined', lookup_expr='year')
    year_joined__gt = django_filters.NumberFilter(field_name='date_joined', lookup_expr='year__gt')
    year_joined__lt = django_filters.NumberFilter(field_name='date_joined', lookup_expr='year__lt')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]
        ordering = ['id']