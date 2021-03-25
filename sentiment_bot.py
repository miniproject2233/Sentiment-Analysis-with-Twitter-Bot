from textblob import TextBlob
import tweepy
def filter(s):
    a=s.split('@')
    b=a[1].split(" ")
    b.pop(0)
    s1=" ".join(b)
    a.pop(1)
    s=" ".join(a)+" " +s1
    return s
#Classificaation system key : daa64450905b79ff28e52174d39880d5f4216cab
#ml = mkl('daa64450905b79ff28e52174d39880d5f4216cab')
#API key :
#pIcQ3bfFAMNdJAIMNCgfHcYOU
#API key secret :
#Ge34vh7BkSwxG7mV5PKRNCLDsgFUKKGzR3fb57gun4EE1agCUk
#Access token :
#1366449162665910272-3Pzn9WAQ4JRxcB0XGIPvmxOKEo1cC8
#Acess token secret :
#Sb1Ax24upv3ErUnaLkEQZYTkMhNA81lhXC3Js8bkkeiPi
API_key='pIcQ3bfFAMNdJAIMNCgfHcYOU'
API_secret='Ge34vh7BkSwxG7mV5PKRNCLDsgFUKKGzR3fb57gun4EE1agCUk'
access_token='1366449162665910272-3Pzn9WAQ4JRxcB0XGIPvmxOKEo1cC8'
access_secret='Sb1Ax24upv3ErUnaLkEQZYTkMhNA81lhXC3Js8bkkeiPi'
auth=tweepy.OAuthHandler(API_key,API_secret)
auth.set_access_token(access_token,access_secret)
bot=tweepy.API(auth)
tweets=bot.mentions_timeline()
class my_tweets:
    def _init_(self, id, text, sentiment,sender):
        self.text = text
        self.id = id
        self.sentiment = sentiment
        self.sender=sender
tweet_sentiment_data=[]

model_id = 'cl_pi3C7JiL'
for i in range(len(tweets)):
    temp=my_tweets(tweets[i].id,filter(tweets[i].text),None,tweets[i].user.screen_name)
    tweet_sentiment_data.append(temp)
def classify_direct(score):
    if score<-0.1:
        return "negative"
    elif score>=-0.1 and score<=0.1:
        return "neutral"
    else:
        return "positive"
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",database="miniproject")
mycursor=db.cursor()
def respond(polarity,subjectivity,id,sender):

    if (polarity<-0.1):
        if(polarity>-0.5):
            bot.update_status("So sorry to hear that! We are constantly trying to improve our services. Do give us another chance, @"+sender,id)
            return ["So sorry to hear that! We are constantly trying to improve our services. Do give us another chance",0,0]
        else:
            bot.update_status("Dear sir/madam, we regret this. We will get in touch to help you feel better right away, please be patient with us, @"+sender,id)
            return ["Dear sir/madam, we regret this. We will get in touch to help you feel better right away, please be patient with us",0,0]
    elif (polarity>=-0.15 and polarity<=0.2):
        if(polarity>=0):
            bot.update_status("Hello. We are here to help. @"+sender,id)
            return ["Hello. We are here to help.",0,0]
        else:
            bot.update_status("Your feedback has been noted @"+sender,id)
            return ["Your feedback has been noted",0,0]
    else:
        if(polarity<0.5):
            bot.create_favorite(id)
            return["",1,0]
        elif(polarity<0.75):
            bot.update_status("We are so glad to hear you are enjoying! Have a great day! @"+sender,id);
            bot.create_favorite(id)
            return["We are so glad to hear you are enjoying! Have a great day!",1,0]
        else:
            bot.update_status("As a company, we feel a lot better when our customers wake up in a positive way. Your services mean a lot to us. Much appreciated. @"+sender,id);
            bot.retweet(id)
            return["As a company, we feel a lot better when our customers wake up in a positive way. Your services mean a lot to us. Much appreciated.",0,1]

#count=int(mycursor.execute("select count(mid) from mentions"))
for i in range(0,len(tweet_sentiment_data)):
    mycursor.execute("select * from mentions where mid="+str(tweet_sentiment_data[i].id))
    check=[]
    for x in mycursor:
        check.append(x)
    if(len(check)==0):
        print("No dupe")
        result = TextBlob(tweet_sentiment_data[i].text)
        tweet_sentiment_data[i].sentiment=(classify_direct(result.sentiment.polarity))
        print("TEXT: "+tweet_sentiment_data[i].text+" | SENTIMENT: "+tweet_sentiment_data[i].sentiment+" | BY: @"+str(tweet_sentiment_data[i].sender))

        string="insert into mentions values("+str(tweet_sentiment_data[i].id)+",'"+str(tweet_sentiment_data[i].text.lower().replace("didn't","did not").replace("can't","cannot").replace("don't","do not").replace("musn't","must not"))+"','"+str(tweet_sentiment_data[i].sender)+"',"+str(result.sentiment.polarity)+","+str(result.sentiment.subjectivity)+")"
        print(string)
        mycursor.execute(string)
    else:
        print("Mention to be skipped")
    mycursor.execute("select * from responses where mid="+str(tweet_sentiment_data[i].id))
    check=[]
    for x in mycursor:
        check.append(x)
    if(len(check)==0):
        result = TextBlob(tweet_sentiment_data[i].text)
        l=respond(result.polarity,result.subjectivity,tweet_sentiment_data[i].id,tweet_sentiment_data[i].sender)
        string="insert into responses values(rid,"+str(tweet_sentiment_data[i].id)+",'"+str(l[0])+"',"+str(l[1])+","+str(l[2])+")"
        mycursor.execute(string)
    else:
        print("Mention to be skipped")

#for twt in reversed(tweet_sentiment_data):
 #   str="Your tweet is "
  #  str=str+(twt.sentiment+" @"+twt.sender)
# bot.update_status(str,twt.id)
