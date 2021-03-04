from monkeylearn import MonkeyLearn as mkl
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
ml = mkl('daa64450905b79ff28e52174d39880d5f4216cab')
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
    def __init__(self, id, text, sentiment):
        self.text = text
        self.id = id
        self.sentiment = sentiment
tweet_sentiment_data=[]
model_id = 'cl_pi3C7JiL'
for i in range(len(tweets)):
    temp=my_tweets(tweets[i].id,filter(tweets[i].text),None)
    tweet_sentiment_data.append(temp)
for i in range(0,len(tweet_sentiment_data)):
    tweet_string_list=[]
    tweet_string_list.append(tweet_sentiment_data[i].text)
    result = ml.classifiers.classify(model_id, tweet_string_list)
    tweet_sentiment_data[i].sentiment=(result.body[0]['classifications'][0]['tag_name'])
    print("TEXT: "+tweet_sentiment_data[i].text+" | SENTIMENT: "+tweet_sentiment_data[i].sentiment)
