from .models import Jobs
from django_filters import FilterSet, CharFilter, ModelMultipleChoiceFilter, ChoiceFilter

FIELD_FILTER = (
    ("cloud", "cloud"),
    ("python", "python"),
    ("db", "db")
)

EXP_FILTER = (
    ("신입", "신입"),
    ("경력", "경력"),
    ("무관", "무관")
)

EDU_FILTER = (
    ("대학교(4년)↑", "대학교(4년)↑"),
    ("대학(2,3년)↑", "대학(2,3년)↑"),
    ("고졸↑", "고졸↑"),
    ("학력무관", "학력무관")
)




class JobFilter(FilterSet):
    job_title = CharFilter(lookup_expr='icontains')
    field = ChoiceFilter(choices=FIELD_FILTER, field_name='field')
    experience = ChoiceFilter(choices=EXP_FILTER, field_name='experience', lookup_expr='icontains')
    edu_level = ChoiceFilter(choices=EDU_FILTER, field_name='edu_level', lookup_expr='icontains')
    # category = ModelMultipleChoiceFilter(
    #     queryset=Jobs.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )

    class Meta:
        model = Jobs
        fields = ['job_title', 'field', 'experience', 'edu_level']


