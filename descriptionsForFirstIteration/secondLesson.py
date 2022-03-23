# Baza Dannix turlari eng mashhur

# SQLite
# PostgreSQL

# Baza Dannix modellardan tashkil topadi.

# Model yaratish

# Modellar prilojeniya ichidagi mmodels.py da yaratiladi

# class Course(models.Model):
#    title = models.CharField(max_length=255)
#    description = models.TextField()
#    price = models.IntegerField()
#    duration = models.IntegerField()
#
#    def __str__(self):
#        return self.title

# models default, CharField, TextField, IntegerFieldlarnik o'zingiz qo'yasiz.

# modellarni ro'yxatdan o'tkazish uchun quyidagi narsa yoziladi

# py manage.py makemigrations
# py manage.py migrate

# prilojeniya ichidagi admin.py ga kirib modellarni registratsiya qilish kerak.

# from .models import Course
#
# admin.site.register(Course)

# keyin superuser yaratish kerak.

# py manage.py createsuperuser