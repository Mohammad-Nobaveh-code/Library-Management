from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail

from .forms import LoginForm, RegisterForm, ContactForm
from book.models import Book, Bookmark
from .models import CustomUser

def main(request):
	books = Book.objects.all()
	paginator = Paginator(books, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	# custom_user_obj = CustomUser.objects.get(user=request.user)
	# bookmark_obj = Bookmark.objects.get(user=custom_user_obj)
	context = {'category': page_obj}
	return render(request, 'main.html', context=context)


def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			info = form.cleaned_data
			user = authenticate(request, username=info['username'], password=info['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('main')
				else:
					return HttpResponse('Invalid account!')
			else:
				return HttpResponse('Invalid login.')
	else:
		form = LoginForm()
	return render(request, 'accounts/login.html', {'form': form})


@login_required
def user_logout(request):
	logout(request)
	messages.info(request, 'you successfully logged out.')
	return redirect('login')
	

def user_register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=True)
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
			return render(request, 'accounts/register_done.html', {'new_user': new_user})
	else:
		form = RegisterForm()
		return render(request, 'accounts/register.html', {'form': form})

def contact_us(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = 'Test'
			body = {
				'first_name': form.cleaned_data['first_name'],
				'last_name': form.cleaned_data['last_name'],
				'email': form.cleaned_data['email'],
				'message': form.cleaned_data['message']
			}
			message = '\n'.join(body.values())

			try:
				send_mail(subject, message, 'admin@gmail.com', ['admin@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid Header found!')
			return redirect('main')
	form = ContactForm()
	return render(request, 'accounts/contact.html', {'form': form})
