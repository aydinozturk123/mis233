from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Count
from json import dumps
from django.shortcuts import redirect
from .forms import SurveyForm
import random

def create(request):
  if request.method == 'POST':
    form = SurveyForm(request.POST)
    choosen_questions = [1, 5, 6, 7, 10, 11, 12, 14, 17, 18, 19, 20]

    if form.is_valid():
      answers = {
        'question1': form.cleaned_data['question1'],
        'question2': form.cleaned_data['question2'],
        'question3': form.cleaned_data['question3'],
        'question4': form.cleaned_data['question4'],
        'question5': form.cleaned_data['question5'],
        'question6': form.cleaned_data['question6'],
        'question7': form.cleaned_data['question7'],
        'question8': form.cleaned_data['question8'],
        'question9': form.cleaned_data['question9'],
        'question10': form.cleaned_data['question10'],
        'question11': form.cleaned_data['question11'],
        'question12': form.cleaned_data['question12']
      }

      user_id = random.randint(3000,9999999)
      for key,value in answers.items():
        question_asked = int(key.split('question')[1])
        answer = Answer(
          userid= user_id,
          questionid= choosen_questions[question_asked-1],
          surveyid= 2020,
          answertext= value
        )
        answer.save()
      return redirect(list_surveys, survey_id=2020)
  

def index(request):
  surveys = Survey.objects.all()
  return render(request, 'survey/index.html', {'surveys': surveys})

def list_surveys(request, survey_id):
  choosen_questions = [1, 5, 6, 7, 10, 11, 12, 14, 17, 18, 19, 20]
  question_asked = int(request.GET.get('question', 1))
  if question_asked <= 0 or question_asked > 12:
    question_asked = 1
  if int(survey_id) <= 2014 or int(survey_id) > 2020:
    survey_id = 2014
  question = Question.objects.get(questionid = choosen_questions[question_asked-1])

  answers = Answer.objects.filter(surveyid=survey_id, questionid=question.questionid)
  answers_grouped = answers.values('answertext').annotate(dcount=Count('answertext'))

  answers_list = [[answer['answertext'], answer['dcount']] for answer in answers_grouped]
  
  if answers.count() != 0:
    answers_list = [list(answers_grouped[0].keys())] + answers_list
    

  next_question = (question_asked+1) if ((question_asked+1)!=13) else 1
  previous_question = (question_asked-1) if ((question_asked-1)!=0) else 12
  context = { 'survey_id': survey_id,
              'question': question,
              'answers': dumps(answers_list),
              'answer_list': answers.order_by('?')[:20],
              'previous_question': previous_question,
              'current_question': question_asked,
              'next_question': next_question
            }
  return render(request, 'survey/results.html', context)

def new_survey(request):
  choosen_questions = [1, 5, 6, 7, 10, 11, 12, 14, 17, 18, 19, 20]
  questions = Question.objects.filter(questionid__in=choosen_questions)
  indexed_questions = []
  for index, obj in enumerate(questions[:12]):
    indexed_questions.append({"index": index+1, "question": obj})
  context = {
    'questions': indexed_questions,
    'ages': range(15,18)
  }
  return render(request, 'survey/submit.html', context)
