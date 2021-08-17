import django_filters
from .models import *
from django_filters import DateFilter

class OrderFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name = "date_created",lookup_expr='gte')
    # end_date = DateFilter(field_name = "date_created",lookup_expr='lte')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer','date_created']

class LendFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name = "date_created",lookup_expr='gte')
    # end_date = DateFilter(field_name = "date_created",lookup_expr='lte')
    class Meta:
        model = Lend
        fields = '__all__'
        exclude = ['student','date_created']

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['price','customer','date_created','tags','description']