from django import forms
from .models import Jobs
import django_filters

class JobFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(lookup_expr='icontains')
    fields = django_filters.ModelMultipleChoiceFilter(queryset=Jobs.objects.values('field'),
                                                      widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Jobs
        fields = ['company', 'field']
