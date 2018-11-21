from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('question/<int:question_id>/', views.question, name='question'),
    path('question/<int:question_id>/results/', views.question_results, name='question_results'),
    path('question/<int:question_id>/vote/<int:choice_id>', views.vote_choice, name='vote_choice'),
    path('question/<int:question_id>/change_state', views.change_question_state, name='change_question_state'),
    path('question/<int:question_id>/remove_choice/<int:choice_id>', views.remove_choice, name='remove_choice'),
    path('question/<int:question_id>/assign_choice/<int:choice_id>', views.assign_choice, name='assign_choice'),
]
