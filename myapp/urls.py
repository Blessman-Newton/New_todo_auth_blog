from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('', views.index, name='index'),
	path('home', views.home, name='home'),
	path('login/', views.login, name='login'),
	path('register/', views.register, name='register'),
	path('blog/', views.blog, name='blog'),
	path('post/<int:pk>', views.post, name='post'),
	path('update/<int:pk>', views.update, name='update'),
	path('delete/<int:pk>', views.delete, name='delete'),
	path('logout/', views.logout, name='logout'),
	path('contact/', views.contact, name='contact'),
	#path('search', views.search, name='search'),
	path('todo/', views.todo, name='todo'),


	path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), 
		name='password_reset'),

	path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), 
		name='password_reset_done'),

	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
	    name='password_reset_confirm'),

	path('reset_password_confirm/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_sent.html'),
	 	name='password_reset_complete'),

]