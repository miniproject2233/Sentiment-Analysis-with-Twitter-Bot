from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="index"),
    path('mention',views.mention,name="mention"),
    path('response',views.response,name="response")
]
