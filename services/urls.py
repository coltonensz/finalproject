from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('job/', views.JobListView.as_view(), name='jobs'),
    path('job/<int:pk>', views.JobDetailView.as_view(), name='job-detail'),

]