import operator
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"index.html",{"key1":"i am from pochinki "})

def result(request):
    article = request.GET['article']
    word = article.split()
    num_count = len(word)
    my_dict = {}
    for words in word:
        if words in my_dict:
            my_dict[words] += 1
        else:
            my_dict[words] = 1
    val_sort = sorted(my_dict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'result.html',{"article":article , "num_count" : num_count, "my_dict": val_sort})


