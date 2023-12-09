from django.urls import path
from . import views

urlpatterns = [
    path('', views.candidate_list, name='candidate_list'),  # Assuming you have a view for listing candidates
    path('<int:pk>/', views.candidate_detail, name='candidate_detail'), # to show the details of candidate
    path('new/', views.candidate_create, name='candidate_create'),# to create new candiddate
    path('<int:pk>/edit/', views.candidate_update, name='candidate_update'),# to edit a existing candidate
    path('<int:pk>/delete/', views.candidate_delete, name='candidate_delete'),# to remove the candidate
]
