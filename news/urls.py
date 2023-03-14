from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('news/', add_news, name='add_news'),
    path('contact/', contact, name='contact'),
    path('logout/', logout, name='logout'),
    path('news/<int:news_id>/', news_detail, name='news')
]