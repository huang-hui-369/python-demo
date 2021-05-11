from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.urls import reverse

from django.template import loader

from django.views import generic

from .models import Question, Choice


# Create your views here.


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)

# ListView 汎用ビューは <app name>/<model name>_list.html というデフォルトのテンプレートを使う
# ListView では、自動的に生成されるコンテキスト変数は question_list になります

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("the question which id is %s does not exist" % question_id)

#     response = "You're looking at the detail of question %s."
#     return HttpResponse(response % question)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {
#         'question': question,
#     })

# DetailView 汎用ビューには、 "pk" という名前で URL からプライマリキーをキャプチャして渡すことになっているので
# デフォルトでは、 DetailView 汎用ビューは <app name>/<model name>_detail.html という名前のテンプレートを使います
# DetailView には question という変数が自動的に渡されます。なぜなら、 Django モデル (Question) を使用していて、

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

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
        # reverse関数を使うと、ビュー関数中での URL のハードコードを防げます。
        # 関数には、制御を渡したいビューの名前と、そのビューに与える URL パターンの位置引数を与えます。
        # この例では、urls.py で設定した URLconf を使っているので、 
        # ex: /polls/5/results/
        # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
        # reverse() を呼ぶと、次のような文字列が返ってきます。
        # '/polls/5/results/'
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
