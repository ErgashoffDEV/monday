# Shablonizatorda ya'ni ekranda biron narsani chiqarish.

# birinchi nimani chiqarmoqchi bo'lsayiz o'shani modellardan import qilasiz
# from .models import Narsa

# keyin funksiya ichida quyidagilarni yozamiz.

# def home(request):
#    narsalar = Narsa.objects.all()
#    return render(request, 'home.html', {'narsalar': narsalar})

# Ko'p ma'lumotlarni ekranda chiqarish uchun sikldan foydalanamiz
# {% for narsa in narsalar %}
# <li>{{narsa}}</li>
# {% endfor %}

# Stillar qo'shish Django

# proyektni ichidagi settings.py ga kiramiz.
# import os tepada import qatorida yozamiz.
# eng oxirgi qatorda esa STATICFILES_DIRS = (os.path.join(BASE_DIR, 'assets'),) ni yozamiz

# bundan kn proyekt ichidagi urls.py ga kiramiz.
# boshida importlar qatorida from django.contrib.staticfiles.urls import staticfiles_urlpatterns shuni yozamiz
# oxirida urlpatterns += staticfiles_urlpatterns() buni yozamiz
# kn assets degan papka ochib, stillarni beramiz

# {% load static from static %} buni html faylga qo'shasiz barcha stillarni olish uchun

# <img src="{% static 'images/monday.svg' %}" alt="Logo"> imageni yo'li

# <link rel="stylesheet" href="{% static 'style.css' %}">

# DRY qo'llanishi bu siz proyekt bo'lmaydi

# templates papkasining ichiga base_layout.html faylini yaratasiz.


# va hech qachon o'zgartirmaydigan qismlar yaratib uni ichiga shuni yozasiz.
# o'zgarmaydigan qismlarga misol: navbar, footer.
# {% block content %}
# {% endblock %}

# boshqa html faylda siz o'zgaruvchi qismlarni yosihiniz mumkin.

# bunda siz barcha narsani shuni ichida yozishingiz shart
# {% block content %}
# {% endblock %}

# {% extends 'base_layout.html' %}
# {% load static from static %} bundan tashqari






