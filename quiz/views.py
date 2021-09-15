from django.shortcuts import render
from .models import Questions,Quiz
from .forms import QuestionForm




def add_question(request):    
    form = QuestionForm(request.POST or None) 
    if form.is_valid():
        form.save()
    context = { 'form': form}

    return render(request, 'quiz/quiz_form.html',context)
def home(request):
    choices = Quiz.objects.all()
    print(choices)
    return render(request,
        'quiz/home.html',
        {'choices':choices})

def questions(request ,choice):
    print(choice)
    flag = 1
    ques = Questions.objects.filter(catagory__name = choice)
    print(ques)
    if not ques:
        flag = 0
    print (flag)
    return render(request,
        'quiz/questions.html',
        {'ques':ques,'flag': flag})

def result(request):
    print("result page")
    flag = 1
    eff = 0
    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Questions.objects.get(id = q)).answer)
            
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1
        # print(qid)
        # print(qans)
        # print(ans)
        print(score)
        if total != 0:
            ef = (score/total)*100
            eff = round(ef,2)
        else :
            flag = 0
    return render(request,
        'quiz/result.html',
        {'score':score,
        'eff':eff,
        'total':total,
        'flag':flag})
def about(request):
    return render(request,
        'quiz/about.html')

def created(request):
    return render(request,
        'quiz/created.html')




#
#
#
#
#
#
#
