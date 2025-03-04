from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver


class TeacherCount(models.Model):
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Teachers count: {self.count}'


class Teacher(models.Model):
    teacher_full_name = models.CharField(max_length=32)
    teacher_picture = models.FileField(upload_to='teacher_picture')
    specialization = models.ForeignKey('Specialization', on_delete=models.CASCADE)
    seniority = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.teacher_full_name}, {self.specialization}, {self.seniority}'


@receiver(post_save, sender=Teacher)
def update_teacher_count(sender, instance, **kwargs):
    count_obj, created = TeacherCount.objects.get_or_create(id=1)
    count_obj.count = Teacher.objects.count()
    count_obj.save()


class Homepage(models.Model):  #  Башкы бет
    school_name = models.CharField(max_length=70, unique=True)  #  Мектептин аты
    image = models.FileField(upload_to='images/')
    title = models.TextField()   #  Мектеп жонундо кыскача

    def __str__(self):
        return self.school_name


class School(models.Model):  # Мектеп
    school_title = models.CharField(max_length=50)
    school_level = models.CharField(max_length=100)  #   Мектек статусу(жалпы,орто)
    school_picture = models.FileField(upload_to='school_pictures')
    school_full_title = models.TextField()  #  Мектеп жонундо толук маалымат
    school_mission = models.TextField()  #  Мектеп миссиясы

    def __str__(self):
        return f'{self.school_title}, {self.school_level}'


class Gallery(models.Model):  #  Мектеп галереясы
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    school_image = models.FileField(upload_to='school_images')  # Мектептин жана класстардын суроттору


class Specialization(models.Model): # Сабактын аты
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.specialization


class Admin(models.Model):
    admin_full_name = models.CharField(max_length=32)
    admin_picture = models.FileField(upload_to='admin_picture')
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)  # Кайсыл сабакты окутат
    job_title = models.CharField(max_length=32) # (Директор, Окуу болум башчысы)

    def __str__(self):
        return f'{self.admin_full_name}, {self.specialization}'


class TeacherCount(models.Model):
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Teachers count: {self.count}'


class Teacher(models.Model):
    teacher_full_name = models.CharField(max_length=32)
    teacher_picture = models.FileField(upload_to='teacher_picture')
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)  # Кайсыл сабакты окутат
    seniority = models.CharField(max_length=20)  # Стаж

    def __str__(self):
        return f'{self.teacher_full_name}, {self.specialization}, {self.seniority}'


@receiver(post_save, sender=Teacher)
def update_teacher_count(sender, instance, **kwargs):
    count_obj, created = TeacherCount.objects.get_or_create(id=1)
    count_obj.count = Teacher.objects.count()
    count_obj.save()


class Timeline(models.Model): # Мектеп хронологиясы
    holiday = models.CharField(max_length=32)
    text = models.TextField()
    class_name = models.CharField(max_length=15)
    date = models.DateField()
    organizer = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.holiday}, {self.organizer}'


class Contact(models.Model):   # Номер
    contact_name = models.CharField(max_length=20)  #(O,MegaCom)
    number = PhoneNumberField(region='KG', null=True, blank=True)  # Номер

    def __str__(self):
        return f'{self.contact_name}, {self.number}'


class Communication(models.Model):   #  Байланыш
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    text = models.CharField(max_length=20) # Байланыш учун
    email = models.EmailField()
    address = models.TextField() # Адрес
    instagram = models.URLField(null=True, blank=True)  # Инстаграм ссылка
    telegram = models.URLField(null=True, blank=True) # Телеграм ссылка

    def __str__(self):
        return f'{self.contact}'


class Qualification(models.Model):  # Квалификация
    document = models.FileField(upload_to='documents', null=True, blank=True)

    def __str__(self):
        return str(self.document)