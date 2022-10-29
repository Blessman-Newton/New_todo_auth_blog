from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .form import MyTodo, BlogForm
from django.contrib.auth.models import User,auth
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.db.models import Q

# Create your views here.
def index(request):
	return render(request, 'index.html')



def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']
		if password == confirm_password:
			if User.objects.filter(email=email).exists():
				messages.info(request, "email already exist")
				return redirect('register')
			elif User.objects.filter(username=username).exists():
				messages.info(request, "username already exist")
				return redirect('register')
			else:
				user = User.objects.create_user(username=username, email=email, password=password)
				user.save()
				return redirect('login')
		else:
			messages.info(request,"password do not much")
			return redirect('register')
	else:
		return render(request, 'register.html')



def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request,user)
			messages.info(request, 'Login Successfully')
			return redirect('home')

		else:
			messages.info(request,'incorrect username and password')
			return redirect('login')
	return render(request, 'login.html')




def logout(request):
	if request.method == 'POST':
		logout(request)
		return HttpResponseRedirect(reverse('login'))



@login_required(login_url='/login/')
def blog(request):
	blog_post = Blog.objects.all()
	page = Paginator(blog_post,3)
	page_list = request.GET.get('page')
	page = page.get_page(page_list)
	post_blog = BlogForm()
	if request.method == 'POST':
		post_blog = BlogForm(request .POST)
		if post_blog.is_valid():
			post_blog.save()
	return render(request, 'blog.html',{'blog_post':blog_post,'page':page, 'post_blog':post_blog})




@login_required(login_url='/login/')
def post(request, pk):
	blog = Blog.objects.get(id=pk)
	return render(request, 'post.html', {'blog':blog})




@login_required(login_url='/login/')
def todo(request):
	blog_post = Blog.objects.all()
	task = Todo.objects.all()
	tasks = MyTodo()
	if request.method == 'POST':
		tasks = MyTodo(request.POST)
		if tasks.is_valid():
			tasks.save()
	return render(request, 'todo.html', {'task': task, 'tasks': tasks})


@login_required(login_url='/login/')
def delete(request, pk):
	task = Todo.objects.get(id=pk)
	task.delete()
	return redirect('todo')



@login_required(login_url='/login/')
def update(request, pk):
	task = Todo.objects.get(id=pk)
	tasks = MyTodo(instance=task)
	if request.method == "POST":
		tasks = MyTodo(request.POST,instance=task)
		if tasks.is_valid():
			tasks.save()
			return redirect('todo')
	return render(request, 'update.html', {'task': task, 'tasks': tasks})



def home(request):
	q = request.GET.get('q') if request.GET.get('q') != None else ''

	blogs = Blog.objects.filter(title__icontains=q)
	return render(request, 'home.html' , {'blogs':blogs})
	


'''different methon for 
Regex/Search functionality 


#def home(request):
#	if request.method == 'GET':
#		q = request.GET.get('q')
#		if q:
#			blogs = Blog.objects.filter(title__icontains=q)
#			return render(request, 'home.html' , {'blogs':blogs})
#		else:
#			return render(request, 'home.html')


'''




def contact(request):
	if request.method == 'POST':
		message_name = request.POST['message_name']
		message_name = request.POST['message_email']
		message_name = request.POST['message']
	
		#send mail
		send_mail(
			message_name , # subject
			message, # message
			message_email, # from email
			['blessmannewton0@gmail.com'], # to email

			)
		return render(request, 'contact.html', {'message_name':message_name })
	else:
		return render(request, 'contact.html')


#def search(request):
#   if request.method == 'POST':
#       search_query = request.POST['search_query']
#       search_post = Blog.objects.filter(title__icontains=search_query)
#       return render(request, 'search.html', {'search_query':search_query, 'search_post':search_post})
#   else:
#       return render(request, 'search.html',{})

    