from django.shortcuts import render_to_response
from django.http import HttpResponse
from posts.forms import AddQuestionForm




def home(request):
    return render_to_response('home.html',locals())
    
def add_question(request):
    if request.method=='POST':
        form=AddQuestionForm(request.POST)
        if form.is_valid():
            return HttpResponse("hello")
        else:
            reg_form=form
            return render_to_response('addquestion.html',locals())
    else:
        form=AddQuestionForm()
        return render_to_response('addquestion.html',locals())    

def unanswered_question(request):
    return render_to_response('answerquestion.html',locals())
    
