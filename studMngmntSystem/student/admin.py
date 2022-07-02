from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'student_age', 'student_father_name', 'student_mother_name', 'gender', 'phone', 'date_of_joining']
    list_display_links = ['student_name']
    pass



class StdYearAdmin(admin.ModelAdmin):
    list_display = ['id', 'year_name', 'year_code']
    list_display_links = ['year_name']



class SemesterAdmin(admin.ModelAdmin):
    list_display = ['id', 'semester_num_name', 'student_year']
    list_display_links = ['semester_num_name']


#
#
# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ['id', 'subj_name', 'stud_class']
#     list_display_links = ['subj_name']

#
# class Student_gradeAdmin(admin.ModelAdmin):
#     list_display = ['id', 'exam_term', 'student', 'subject', 'student', 'subject','total_mark', 'mark']
#     list_display_links = ['exam_term']
#


admin.site.register(StdYear, StdYearAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Subject)
admin.site.register(Mark)
# admin.site.register(Student_grade, Student_gradeAdmin)





