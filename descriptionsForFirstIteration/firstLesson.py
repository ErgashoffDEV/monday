# Django = MTV = Model Template View

# Model = oshxona
# Template = ofitsiant
# View = buterbrod

# Djangoda ish boshlamoqchi bo'lsangiz shularni barchasi bo'lishi shart

# Djangoda proyekt yaratish
# django-admin startproject proyekt_nomi

# Proyektni ichida albatta prilojeniya bo'lishi shart
# py manage.py startapp prilojeniya_nomi

# Keyin proyektni ichidagi settings.pyga kirib, uning ichidagi INSTALLED_APPSga prilojeniyani nomini yozasiz

# Undan keyin prilojeniya ichida urls.py papkasini hosil qilamiz.
# urls.pyda shu narsa yoziladi

# from django.urls import path
# urlpatterns = []

# keyin proyektni ichidagi urls.pyga kirib, includeni import qilamiz.
# shunday bo'lishi kk

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(('prilojeniya_nomi.urls', 'proyekt_nomi'), namespace='prilojeniya_nomi'))
# ]

# yangi page hosil qilish Djangoda pastda ko'rsatilgan

# from . import views
# from django.urls import path

# urlpatterns = [
#    path('', views.home) yangi page nomi home views default znacheniya. '' > bu esa path
# ]

# Keyin prilojeniya ichida templates papkasini yaratib html fayl qo'shamiz.

# views.py ga kirib funksiya yaratamiz.

# from django.shortcuts import render
#
# def home(request):
#    return render(request, 'home.html', {})

# run qilish >>>>>> py manage.py runserver




