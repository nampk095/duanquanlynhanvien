from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
# Create your views here.



def viewlist(request):
    #get_object_or_404(Question, pk=1) Question.objects.all()
    list_question = Question.objects.all()
    context = {"dsquest": list_question}
    return render(request, "polls/question_list.html", context)


def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {"qs": q})

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu = request.POST["choice"]
        c = q.choice_set.get(pk=dulieu)

    except:
        HttpResponse("loi khong co choice nay dau")
    c.vote = c.vote + 1
    c.save()
    return render(request, "polls/result.html", {"q":q})