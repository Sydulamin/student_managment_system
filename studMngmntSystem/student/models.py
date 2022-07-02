from django.db import models
import string, random
# from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User


CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]




def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))





class StdYear(models.Model):
    year_code = models.CharField(max_length=15, null=True, blank=True)
    year_name = models.CharField(max_length=100)

    class Meta():
        verbose_name_plural = 'University Year'

    def __str__(self) -> str:
        return self.year_name

    def save(self, *args, **kwargs):
        print('A new year record is created!')
        print('Year Code:', self.year_code)
        if self.year_code == None:
            print('Generate a new random string for the year code!')
            self.year_code = random_string_generator()

        super(StdYear, self).save(*args, **kwargs)




class Semester(models.Model):
    semester_num_name = models.CharField(verbose_name='Semester', max_length=100)
    student_year = models.ForeignKey(StdYear, verbose_name='Year', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.semester_num_name





class Student(models.Model):
    student_name = models.CharField(max_length=100, null=True, blank=True)
    student_age = models.PositiveIntegerField(null=True, blank=True)
    student_father_name = models.CharField(max_length=100, null=True, blank=True)
    student_mother_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=CHOICES, default='Male')
    phone = models.CharField(max_length=25, null=True, blank=True)
    date_of_joining = models.DateField(verbose_name='Admission', default=timezone.now)
    # year_id = models.ManyToManyField(StdYear, verbose_name='Year', null=True, blank=True)

    semester_id = models.ForeignKey(Semester, verbose_name='Semester', on_delete=models.CASCADE)

    student_image = models.FileField(upload_to="student-image/", default="student-image/person_avatar.png", blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self) -> str:
    #     return self.student_name



class Subject(models.Model):
    subj_name = models.CharField(max_length=100)
    # stud_class = models.ForeignKey(StdClass, on_delete=models.CASCADE)
    subj_credit = models.FloatField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    total_mark = models.FloatField()

    def __str__(self) -> str:
            return self.subj_name



class Mark(models.Model):
    mark_code = models.CharField(max_length=20, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    obtained_mark = models.FloatField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    # #######################################
    # [ Error: The issue was trying to show the 'obtained_mark' as the str-representation of this model class, but a float-value cannot be represent as a string ]
    # #######################################

    def __str__(self) -> str:
            return self.mark_code

    def save(self, *args, **kwargs):
        if self.mark_code == None:
            self.mark_code = self.student.student_name + '_' + self.subject.subj_name + '_' + random_string_generator()

        super(Mark, self).save(*args, **kwargs)




#
# class Student_grade(models.Model):
#     exam_term = models.CharField(max_length=100)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     total_mark = models.FloatField()
#     mark = models.FloatField()
#
#
#
