from django.urls import path
from . import views


app_name = 'studentApp'

urlpatterns = [
    # path('', views.student, name='student'),
    # path('create-student/', views.createStudent, name='createStudent'),
    path('update-student-info/', views.updateStudentInfo, name='updateStudentInfo'),
    # path('remove-student/<str:std_id>/', views.studentRemove, name='studentRemove'),
    # path('update-student/<str:std_id>/', views.studentUpdate, name='studentUpdate'),
]