from django.shortcuts import render
from .decorators import *
from student.models import *
from django.contrib.auth.models import User



@stop_unauthenticated_users
@allow_admins_only
def adminPage(request):

    student = Student.objects.all()
    # for s in student:
    #     print(s.semester_id)
    semester = Semester.objects.all()


    if request.method == 'POST':

        # print('Semester Name:', request.POST['semester'])
        sem_var = request.POST['semester']
        try:
            semester_query = Semester.objects.get(semester_num_name=sem_var)
        except:
            semester_query = Semester.objects.get(semester_num_name="1st Sem")
        # print('Semester Query:', semester_query)

        try:
            Student.objects.create(
                student_name=request.POST['student_name'],
                student_age=request.POST['student_age'],
                student_father_name=request.POST['student_father_name'],
                student_mother_name=request.POST['student_mother_name'],
                gender=request.POST['gender'],
                phone=request.POST['student_phone'],
                semester_id=semester_query,
                student_image=request.FILES['image'],
            )
        except:
            Student.objects.create(
                student_name=request.POST['student_name'],
                student_age=0,
                student_father_name=request.POST['student_father_name'],
                student_mother_name=request.POST['student_mother_name'],
                gender=request.POST['gender'],
                phone=request.POST['student_phone'],
                semester_id=semester_query,
            )


    context = {
        'student': student,
        'semester': semester,
    }

    return render(request, 'rolesPermsApp/adminPage.html', context)



def student_update(request, stud_id):
    print('Student ID:', stud_id)
    stud_query = Student.objects.get(pk=stud_id)

    semester = Semester.objects.all()

    if request.method == "POST":
        semester_query = Semester.objects.get(semester_num_name=request.POST['semester'])

        stud_query.student_name = request.POST['student_name']
        stud_query.student_age = request.POST['student_age']
        stud_query.student_father_name = request.POST['student_father_name']
        stud_query.student_mother_name = request.POST['student_mother_name']
        stud_query.gender = request.POST['gender']
        stud_query.phone = request.POST['student_phone']
        stud_query.semester_id = semester_query
        stud_query.save()

        return redirect('rolesPermsApp:adminPage')

    context = {
        'student':stud_query,
        'semester': semester,
    }
    return render(request, 'rolesPermsApp/adminPage_stud_update.html', context)



def student_delete_confirmation_page(request, id):
    stud_query = Student.objects.get(pk=id)

    context = {
        'student': stud_query,
    }

    return render(request, 'rolesPermsApp/adminPage_stud_delete.html', context)



def student_delete(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect("rolesPermsApp:adminPage")



@stop_unauthenticated_users
@allow_staff_only
def staffPage(request):
    return render(request, 'rolesPermsApp/staffPage.html')


@stop_unauthenticated_users
@allow_student_only
def studentPage(request, id):
    print("Student page func:", id)
    user = User.objects.get(id=id)
    student = Student.objects.get(user_id=user)
    context = {
        'student': student,
    }
    return render(request, 'student/studentPage.html', context)


@stop_unauthenticated_users
def commonPage(request):
    return render(request, 'rolesPermsApp/commonPage.html')
