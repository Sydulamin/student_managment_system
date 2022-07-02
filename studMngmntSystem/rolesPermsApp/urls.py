from django.urls import path
from . import views


app_name = 'rolesPermsApp'

urlpatterns = [
    path('admin-page/', views.adminPage, name='adminPage'),
    path('admin-page/sutd-info-update/<str:stud_id>/', views.student_update, name='adminPage_stud_update'),
    path('admin-page/sutd-record-delete-confirmation-page/<str:id>/', views.student_delete_confirmation_page, name='adminPage_stud_delete_confirmation'),
    path('admin-page/sutd-info-delete/<str:id>/', views.student_delete, name='adminPage_stud_delete'),

    path('staff-page/', views.staffPage, name='staffPage'),
    path('stud-page/<str:id>/', views.studentPage, name='studPage'),
    path('common-page/', views.commonPage, name='commonPage'),
]
