from django import forms


class StudentUpdateForm(forms.Form):
    student_name = forms.CharField(max_length=100)
    student_age = forms.IntegerField()
    student_father_name = forms.CharField(max_length=100)
    student_mother_name = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=10)
    phone = forms.CharField(max_length=20)
