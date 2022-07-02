from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from student.models import Student, Semester


@receiver(post_save, sender=User)
def create_student_profile(sender, instance, **kwargs):
    print("A signal is ready to create student profile!")
    print('sender:', sender)
    print('instance:', instance)
    print('**kwargs:', kwargs)

    # Check if user is successfully created
    if kwargs['created'] == True:
        print("User Active:", instance.is_active)
        print("User Staff:", instance.is_staff)
        print("User Admin:", instance.is_superuser)
        print(instance.username)


        # Check if user'r permission "active" is True
        if (instance.is_active == True) and (instance.is_staff == False) and (instance.is_superuser == False):
            print('Create a new student profile!')
        #     print("User ID:", instance.id)
        #
        #     # for u in dir(instance):
        #     #     print(u)
        #     #
            sem1 = Semester.objects.get(semester_num_name="1st Semester")
        #
            Student.objects.create(
                user_id=instance,
                student_name=instance.username,
                semester_id=sem1,
            )

