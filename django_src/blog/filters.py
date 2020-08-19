from django import forms
from .models import Jobs
from django_filters import FilterSet, CharFilter, ModelMultipleChoiceFilter, ChoiceFilter


JOB_FIELD = (
    (0, "cloud"),
    (1, "python"),
    (2, "db")
)
# job_title = CharFilter(lookup_expr='icontains')

class JobFilter(FilterSet):
    job_title = CharFilter(lookup_expr='icontains')
    field = ChoiceFilter(choices=JOB_FIELD)
    category = ModelMultipleChoiceFilter(
        queryset=Jobs.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


    class Meta:
        model = Jobs
        fields = ['job_title', 'field', 'category']


