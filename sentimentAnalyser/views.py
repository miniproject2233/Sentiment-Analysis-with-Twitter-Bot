from django.shortcuts import render
from django.http import HttpResponse
from .apps import SentimentanalyserConfig
from textblob import TextBlob
from .models import Mentions
from .models import Responses
def home(request):
    def respond(polarity):
        if (polarity<-0.1):
            if(polarity>-0.5):
                return ["So sorry to hear that! We are constantly trying to improve our services. Do give us another chance"]
            else:
                return ["Dear sir/madam, we regret this. We will get in touch to help you feel better right away, please be patient with us",0,0]
        elif (polarity>=-0.15 and polarity<=0.2):
            if(polarity>=0):
                return ["Hello. We are here to help.",0,0]
            else:
                return ["Your feedback has been noted",0,0]
        else:
            if(polarity<0.5):
                return["",1,0]
            elif(polarity<0.75):
                return["We are so glad to hear you are enjoying! Have a great day!",1,0]
            else:
                return["As a company, we feel a lot better when our customers wake up in a positive way. Your services mean a lot to us. Much appreciated.",0,1]
    text=request.POST.get('data','')
    if(text==''):
        text='-'
        reply='-'
        sentiment='-'
        prediction='-'
    else:
        text=TextBlob(text)
        prediction=text.sentiment.polarity
        prediction=round(prediction,2)
        reply=respond(prediction)[0]
        if prediction<0:
            sentiment='Negative'
        elif prediction==0:
            sentiment='Neutral'
        else:
            sentiment='Positive '
    return render(request,'index.html',{'text':text,'result':reply,'polarity':prediction,'sentiment':sentiment})


def mention(request):
    mention=Mentions.objects.all()
    response=Responses.objects.all()
    return render(request,'mentions.html',{'mention':mention})
def response(request):
    response=Responses.objects.all()
    return render(request,'responses.html',{'response':response})