from django.http import HttpResponse 
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def acerca(request):
    return render(request, 'acerca.html')
         
def contador(request):
    fulltext = request.GET['texto'] 

    wordlist = fulltext.split()

    worddictionary ={}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] =1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    
    return render(request, 'contador.html', {'fulltext': fulltext, 'contador':len(wordlist),
    'sortedwords': sortedwords})

         