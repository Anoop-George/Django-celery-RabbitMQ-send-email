from django.urls import path

from core import views


urlpatterns = [
    path('',views.index)
    # url(r'^$', views.UsersListView.as_view(), name='users_list'),
    # url(r'^generate/$', views.GenerateRandomUserView.as_view(), name='generate'),
]