from polls.models import Question,Choice
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from polls.forms import QuestionForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def about(request):
    return HttpResponse("Hello, world. i m learning django.")

def contact(request):
    return HttpResponse("Hello, my <b>email is asmita@gmail.com</b>.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question,'title':'Nepal Election','sitename':'Election of Nepal'})

def choice(request):
    latest_choice_list = Choice.objects.all()
    context = {'latest_choice_list': latest_choice_list,'title':'select choice','sitename':'my choice'}
    return render(request, 'polls/choice.html', context)
   #latest_question_list = Question.objects.order_by('-pub_date')[:5]
   #latest_choice_list = Choice.objects.all()
   # output = ', '.join([q.choice_text for q in latest_choice_list])
   # return HttpResponse(output)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question,'title':'select choice','sitename':'my choice'})

def add_poll(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            questions = Question.objects.all()
            return render(request, 'polls/index.html', {'questions': questions})
        else:
            print(form.errors)
    else:
        form = QuestionForm()
    return render(request, 'polls/add_poll.html', {'form': form})



