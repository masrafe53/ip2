from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name = 'home'),
    path('blog_post/',views.blog_post,name = 'blog_post'),
    path('generate_social_post/',views.generate_social_post,name='generate_social_post'),
    path('generate_description/',views.generate_description,name='generate_description'),

]