from django.urls import path
from . import views

urlpatterns = [
    path('search_teacher_by_name/', views.search_teacher_by_name, name='search_teacher_by_name/'),
    path('search_teacher_by_department/', views.search_teacher_by_department, name='search_teacher_by_department/'),
]

