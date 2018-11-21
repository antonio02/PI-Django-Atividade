from django.shortcuts import render, redirect
from .models import Question, Choice

# Create your views here.

def index(request):
    return render(request, 'index.html', {'questions': Question.objects.order_by('-pub_date')})

def question(request, question_id):
    return  render(request, 'question.html', {'question': Question.objects.get(id=question_id),
                                              'unassigned_choices': Choice.objects.filter(question=None)})

def question_results(request, question_id):
    return render(request, 'question_results.html', {'question': Question.objects.get(id=question_id)})

def vote_choice(request, question_id, choice_id):
    if not Choice.objects.get(id=choice_id).question.closed:
        Choice.objects.get(id=choice_id).up_vote()

    return redirect(question, question_id)

def change_question_state(request, question_id):
    Question.objects.get(id=question_id).change_state()
    return redirect(question, question_id)

def remove_choice(request, question_id, choice_id):
    Question.objects.get(id=question_id).choices.get(id=choice_id).remove_from_question()
    return redirect(question, question_id)

def assign_choice(request, question_id, choice_id):
    choice = Choice.objects.get(id=choice_id)
    if choice.question == None:
        choice.question = Question.objects.get(id=question_id)
        choice.save()
    return redirect(question, question_id)

