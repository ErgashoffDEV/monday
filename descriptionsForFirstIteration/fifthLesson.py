# Forma yaratish Djangoda.

# birnchi bo'lib models.pyda model yaratish kk

# class Application(models.Model):
# client_name = models.CharField(max_length=255)
# client_phone_number = models.CharField(max_length=255)

# modelda sizda qanaqa polyalar bo'lishini aytib o'tib ketasiz.

# keyin uni admins.pyga kirib reg qilasiz

# birinchi import qilasiz keyin admin.site.register(Admin) shuni yozasiz

# keyin prilojeniyada forms.py degan papka ochib, uni ichiga shularni yozasiz.

# from django import forms import bo'lishi shart
# from .models import Application bu models.pyda yaratgan modelizni import qilasiz

# class ApplicationForm(forms.ModelForm):
#    class Meta:
#        model = Application          model nomini yozasiz
#        fields = ['client_name', 'client_phone_number']    bunga modelda keltirilgan fieldlarni yozasiz


# formaning oddiy ishlash logikaksi.

# form = ApplicationForm(request.POST or None)
#    is_success = False
#    if request.method == 'POST' and form.is_valid():
#        is_success = True
#        form.save()
#        form = ApplicationForm()
#    return render(request, 'about.html', {'course': course, 'form': form, 'is_success': is_success})

# {% if is_success %}
#    <div class="notification is-success is-size-3 has-text-centered">
#        <button class="delete"></button>
#        Ваша заявка принята! Спасибо!
#    </div>
# {% endif %}

# shablonizatorda shu narsani quyish kerak notification paydo bulishi uchun




