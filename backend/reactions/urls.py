from django.urls import path, include

from reactions import views

urlpatterns = [
    path('reactions', views.ReactionsList.as_view())
]
