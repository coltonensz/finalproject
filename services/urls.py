from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.index, name='index'),
    path('/services/#', contact_view, name='contact'),
    path('job/', views.JobListView.as_view(), name='jobs'),
    path('job/<int:pk>', views.JobDetailView.as_view(), name='job-detail'),

]