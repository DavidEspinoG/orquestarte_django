from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views import View

# class SignUp(CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/signup.html'

#     def get_success_url(self):
#         return reverse_lazy('login')
    
#     def get_form(self, form_class=None):
#         form = super(SignUp, self).get_form()
#         form.fields['username'].widget = forms.TextInput(attrs={'class':'', 'placeholder': 'Nombre de usuario'})
#         form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'', 'placeholder': 'Contraseña'})
#         form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'', 'placeholder': 'Repite la contraseña'})
#         return form

class SignUp(View):
    def get(self, request):
        return render(request, 'registration/signup.html')
    def post(self, request): 
        username = request.POST['username']
        user_mail = request.POST['user_mail']
        password = request.POST['password']
        user = User.objects.create_user(username, user_mail, password)
        user.save()
        return redirect('/')

def loginView(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request,user)
            return redirect('/')
        else:
            context = {'errores': "Usuario o contraseña incorrecto"}
            return render(request, 'registration/login.html', context)
    else: 
        return render(request, 'registration/login.html')