from django.shortcuts import render
from myapp1.models import Text
from myapp1.models import Answer
import random

# Create your views here.

text = Text(text='_NOTEXT_')

def index_page(request):

    global text
    button = request.GET.get('name')
    if(button == 'Нейтральный'):
        ans = Answer(name=text.text, answer = 0)
        ans.save()
    elif(button == 'Непредвзятый'):
        ans = Answer(name=text.text, answer = 1)
        ans.save()
    elif(button == 'Предвзятый'):
        ans = Answer(name=text.text, answer = 2)
        ans.save()
    else:
        print("\/"*25)

    text = Text.objects.get(id=random.randint(1,6))
    

    return render(request, 'index.html', {'text': text})