from django.shortcuts import render, redirect
from django.http import HttpResponse,  HttpResponseRedirect
from learn.models import Word, Werb, User
from django.urls import reverse
from django.template import loader
import json
import random
from django.utils import timezone
import datetime
from django.contrib.auth import authenticate, login

from .forms import RegisterForm

data_js = {}
w  = ""
werb_true = "" # True - vybrane je sloveso, False - vybrane je slovo
word = "" # "*"- obsahuje slovo
ind = 0 # True - hrac hada slovo, False - hrac hada preklad, 0 - zakladne nastavenie
correct = True # True - odpoved je spravna, False - odpoved je nespravna
dark_mode = True # True - cierny rezim, False - normalny rezim







    
def mode(request):
    global dark_mode
    if dark_mode == True:
        dark_mode = False
    else:
        dark_mode = True
    template = request.POST.get("mode")
    return HttpResponseRedirect(reverse('learn:index'))
    
    
    

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {"dark_mode":dark_mode}
    context.update({"form":form})
    template = loader.get_template('learn/register.html')
    return HttpResponse(template.render(context, request))


        
def index(request):
    global user
    global ind
    global word
    global werb_true
    global w
    error = False
    list_of_words = []
    words = Word.objects.all()
    werbs = Werb.objects.all()
    template = loader.get_template('learn/index.html')
    context = {"dark_mode":dark_mode}


    try:
        for i in words:
            if i in request.user.word.all():
                if timezone.now() - i.date >= datetime.timedelta(days=0):
                    list_of_words.append(i)

        for i in werbs:
            if i in request.user.werb.all():
                if timezone.now() - i.date >= datetime.timedelta(days=0):
                    list_of_words.append(i)
    except:
        return HttpResponse(template.render(context, request))
    try: 
        word = random.choice(list_of_words)
        ind = random.randint(0,1)
        if ind == 0:
            ind = True
            w = word.word
        else:
            ind = False
            w = word.translation
        

        try:
            if word.tri_os:
                werb_true = True
        except:
            werb_true = False
    except:
        error = "You hove no words"
    

    
    context = {
        "dark_mode":dark_mode,
        "werb_true": werb_true,
        'ind': ind,
        "w":w,
        "error":error
    }
    return HttpResponse(template.render(context, request))

def check(request,):
    global data_js
    global correct
    one_is_correct = False
    two_is_correct  = False
    three_is_correct  = False
    four_is_correct  = False

    template = loader.get_template('learn/check.html')
    context = {"dark_mode":dark_mode}
    context.update({"werb_true": werb_true})

    if werb_true == True:
        if ind == 0:
            pass
        else:
            pass
        word_ = request.POST.get("word").lower()
        P_cas = request.POST.get("Pritomny_cas").lower()
        M_cas = request.POST.get("Mynuly_cas").lower()
        preklad = request.POST.get("preklad").lower()

        if word_ == word.word:
            one_is_correct = True
            context.update({"one_is_correct":one_is_correct})
        else:
            correct = False
            
        if P_cas == word.tri_os:
            two_is_correct = True
            context.update({"two_is_correct":two_is_correct})

        else:
            correct = False
            
        if M_cas == word.minuly_cas:
            three_is_correct = True
            context.update({"three_is_correct":three_is_correct})
        else:
            correct = False
            
            new_M_cas = word.minuly_cas
        if preklad == word.translation:
            four_is_correct = True
            context.update({"four_is_correct":four_is_correct})
        else:
            correct = False
            
        
        data_js.update({"a":word.word})
        data_js.update({"b":word.tri_os})
        data_js.update({"c":word.minuly_cas})
        data_js.update({"d":word.translation})

        js_data = str(json.dumps(data_js))
        context.update({"data_js":js_data})
        context.update({"word_":word_})
        context.update({"P_cas":P_cas})
        context.update({"M_cas":M_cas})
        context.update({"preklad":preklad})

    else:

        
        word_ = request.POST.get("word")
        preklad = request.POST.get("preklad").lower()

        if word_ == word.word:
            one_is_correct = True
            
            context.update({"one_is_correct":True})
        else:
            correct = False
        if preklad == word.translation:
            four_is_correct = True
            context.update({"four_is_correct":four_is_correct})
        else:
            correct = False
        
        context.update({"word_": word_})
        context.update({"preklad": preklad})

        data_js.update({"a":word.word})
        data_js.update({"b":word.translation})

        js_data = str(json.dumps(data_js))
        context.update({"data_js":js_data})

    if correct == True:
        word.tries = word.tries + 1
        word.save()
        
        
        if word.tries == 3: 
            word.level = word.level + 1
            word.save()
            if word.level == 2:
                word.date = timezone.now() + datetime.timedelta(days=2)
                word.save()
            elif word.level == 3:
                word.date = timezone.now() + datetime.timedelta(days=4)
                word.save()
            elif word.level == 4:
                word.date = timezone.now() + datetime.timedelta(days=7)
                word.save()
            elif word.level == 5:
                word.delete()

            word.tries = 0
            word.save()
    else:
        word.level = 1
        word.tries = 0
        word.save()
    
    context.update({"one_is_correct":one_is_correct})        
    return HttpResponse(template.render(context, request))   
    #return HttpResponseRedirect(reverse('learn:check', args = (context)))

def add(request):

    if request.method == "POST":
        
        newItem = request.POST.get("newitems")
        items = newItem.split("-")
        if len(items)>1:
            
            if len(items)> 3:
                
                w = Werb(word = items[0], tri_os = items[1], minuly_cas = items[2], translation=items[3], date = timezone.now(), user = request.user)
                w.save()
                request.user.werb.add(w)
            else:
                
                w = Word(word = items[0], translation=items[1], date = timezone.now(), user = request.user)
                w.save()
                request.user.word.add(w)
            
            return HttpResponseRedirect(reverse('learn:add'))
            
    template = loader.get_template('learn/add.html')
    context = {"dark_mode":dark_mode}

    words = Word.objects.all()
    werbs = Werb.objects.all()
    list_of_words = []
    list_of_werbs = []
    try:
        for i in words:
            if i in request.user.word.all():
                list_of_words.append(i)
        for i in werbs:
            if i in request.user.werb.all():
                list_of_werbs.append(i)
    except:
        return HttpResponse(template.render(context, request))
    
    context.update({"words": list_of_words})
    context.update({"werbs": list_of_werbs})
    
    return HttpResponse(template.render(context, request))

    



def delete(request, werb_id= 0, word_id = 0):

    context = {"dark_mode":dark_mode}

    if werb_id>0:
        
        try:
            w = Werb.objects.get(pk=werb_id)
            if w in request.user.werb.all():
                Werb.objects.get(pk=werb_id).delete()
        except:
            pass      

            
    else:
        try:
            w = Word.objects.get(pk=word_id)
            if w in request.user.word.all():
                Word.objects.get(pk=word_id).delete()
        except:
            pass
   
    return HttpResponseRedirect(reverse('learn:add'))
    
def detail(request,  werb_id= 0, word_id = 0):
    context = {"dark_mode":dark_mode}
    template = loader.get_template("learn/detail.html")
    word = 0
    if werb_id>0:
        werb_true1 = True
        try:
            w = Werb.objects.get(pk=werb_id)
            if w in request.user.werb.all():
                word = w
        except:
            pass    
        
    else:
        werb_true1 = False
        try:
            w = Word.objects.get(pk=word_id)
            if w in request.user.word.all():
                word = w
        except:
            pass
    if word == 0:
        return HttpResponseRedirect(reverse('learn:add'))

    context.update({"werb_true":werb_true1})
    context.update({"word":word})

    return HttpResponse(template.render(context, request))
    
def change(request,  word_id = 0 , werb_id = 0,):
    
    
    if word_id == 0:
        word = Werb.objects.get(pk=werb_id)
        to_change = request.GET.get("word").lower()
        if to_change != "":
            new = to_change
            word.word = new
            word.save()
        to_change = request.GET.get("p").lower()
        if to_change != "":
            new = to_change
            word.tri_os = new
            word.save()
        to_change = request.GET.get("m").lower()
        if to_change != "":
            new = to_change
            word.minuly_cas = new
            word.save()
        to_change = request.GET.get("preklad").lower()
        if to_change != "":
            new = to_change
            word.translation = new
            word.save()
    else:
        word = Word.objects.get(pk=word_id)
        to_change = request.GET.get("word")
        if to_change != "" :
            new = to_change
            word.word = new
            word.save()
        to_change = request.GET.get("word").lower()
        if to_change != "":
            new = to_change
            word.translation = new
            word.save()
    
    return HttpResponseRedirect(reverse('learn:add'))