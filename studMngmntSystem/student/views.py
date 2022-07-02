from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import StudentUpdateForm


def student(request):
    student = Student.objects.all()
    # print('Student:', student)
    context = {
        'student': student,
    }
    return render(request, 'student/student.html', context)


def createStudent(request):
    if request.method == 'POST':
        print('A new student record is created!')

        print('Student Name:', request.POST['student_name'])
        print('Student Age:', request.POST['student_age'])

        Student.objects.create(
            student_name=request.POST['student_name'],
            student_age=request.POST['student_age'],
        )

        return redirect('studentApp:student')


# def studentRemove(request, std_id):
#     print('Student ID (Student Remove function):', std_id)
#     student = Student.objects.get(pk=std_id)
#     student.delete()
#     return redirect('studentApp:student')
#
#
# def studentUpdate(request, std_id):
#     print('Student ID (Student Update function):', std_id)
#     student = Student.objects.get(pk=std_id)
#     student.delete()
#     return redirect('studentApp:student')

def updateStudentInfo(request):
    Student_Update_Form = StudentUpdateForm()

    if request.method == "POST":
        print("Student name:", request.POST['student_name'])
        print("Student age:", request.POST['student_age'])
        print("Student father name:", request.POST['student_father_name'])
        print("Student mother name:", request.POST['student_mother_name'])
        print("Student gender:", request.POST['gender'])
        print("Student phone:", request.POST['phone'])


    #     ##########################
    # Code here: update the student record
    #     ##########################



    context = {
        'Student_Update_Form': Student_Update_Form,
    }
    return render(request, 'student/studentInfoUpdate.html', context)