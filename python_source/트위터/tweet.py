import oauth2
import json
import datetime
import time
from config import *

def oauth2_request(consumer_key, consumer_secret, access_token, access_secret):
    try:
        consumer=oauth2.Consumer(key=consumer_key, secret=consumer_secret)
        token=oauth2.Token(key=access_token,secret=access_secret)
        client=oauth2.Client(consumer,token)
        return client
    except Exception as e:
        print(e)
        return None
def get_user_timeline(client, screen_name, count, include_rts='False'):
    base="http://api.twitter.com/1.1"
    node="/statuses/user_timeline.json"
    fields="?screen_name=%s&count=%s&include_rts=%s" \
            %(screen_name,count, include_rts)
    url =base+node+fields
    response,data=client.request(url)
    try:
        if response['status']=='200':
            return json.loads(data.decode('utf-8'))
    except Exception as e:
            print(e)
            return None
def getTwitterTwit(tweet,jsonResult):
    tweet_id=tweet['id_str']
    tweet_message='' if 'text' not in tweet.keys() else tweet['text']
    screen_name='' if 'user' not in tweet.keys()\
                 else tweet['user']['screen_name']
    tweet_link=''
    if tweet['entities']['urls']:
        for i, val in enumerate(tweet['entities']['urls']):
            tweet_link=tweet_link+tweet['entities']['urls'][i]['url']+ ''
    else:
        tweet_link=''
    num_favorite_count= 0 if 'favorite_count' not in tweet.keys()\
                        else tweet['favorite_count']
    num_shares = 0 if 'retweet_count' not in tweet.keys()\
                 else tweet['retweet_count']
    num_likes=num_favorite_count
    jsonResult.append({'post_id':tweet_id,
                       'message':tweet_message,
                       'name':screen_name,
                       'link':tweet_link,
                       'num_reactions':num_favorite_count,
                       'num_shares':num_shares,
                       'num_likes':num_likes,
                       })
def main():
    screen_name="jtbc_news"
    num_posts=50
    jsonResult=[]
    client=oauth2_request(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET)
    tweets=get_user_timeline(client,screen_name,num_posts)
    #for tweet in tweets:
       # getTwitterTwit(tweet,jsonResult)
    with open('%s_twitter.json'%(screen_name),'w',encoding='utf8')as outfile:
        str_=json.dumps(jsonResult,
                        indent=4,
                        sort_keys=True,
                        ensure_ascii=False)
        outfile.write(str_)
    print('%s_twitter.json SAVED' %(screen_name))
if __name__=='__main__':
    main()
