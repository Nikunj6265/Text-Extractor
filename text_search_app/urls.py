from django.urls import path
from .views import *
urlpatterns = [
     path('register/', RegistrationView.as_view(), name='register'),
     path('login/', LoginView.as_view(), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),
     path('word-search/', SearchParagraphs.as_view(), name='word-search'),
     path('insert-text/', InsertParagraphs.as_view(), name='insert-text'),
     path('update-details/', UserDetailView.as_view(), name='update-details'),
]