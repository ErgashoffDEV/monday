# Marshrutrizatsiya saytning asosiy qismi hisoblanadi.
# Marshrutrizatsiya faqatgina urls.py dagi urlpatterns ichida yoziladi.

# bu uch qismdan iborat 2ta asosiy va bitta kerak emas

# path('about/', views.about, name='about')
# path( route,    views,      name)

# Yangi path qo'shish
# path('narsa', views.narsa, name='narsa'
# kn views.pyda funksiya yaratishingiz kk buladi

# def about(request):
#    narsa = Course.objects.all()
#    return render(request, 'narsa.html', {'narsa': narsa})

# A hrefga yo'nalish berish Djangoda

# <a href="{% url 'landing:about' course.pk %}"> </a>
