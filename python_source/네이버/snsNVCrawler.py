import os
import sys
import urllib.request
import datetime
import time
import json
from config import *

#[CODE 1]
def get_request_url(url):
    
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    
    #이곳에 프로그램을 작성하세요.
    try:
        response=urllib.request.urlopen(req)
        if response.getcode()==200:
             print("[%s] Url Request Success"% datetime.datetime.now())
             return response.read().decode('utf-8')
        
       
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s"%(datetime.datetime.now(),url))
        return None

    

#[CODE 2]
def getNaverSearchResult(sNode, search_text, page_start, display): 
    #이곳에 프로그램을 작성하세요.
    base="https://openapi.naver.com/v1/search"
    node="/%s.json"%sNode
    parameters="?query=%s&start=%s&display=%s"%(urllib.parse.quote(search_text),page_start,display)
    url=base+node+parameters
    retData=get_request_url(url)
    if(retData==None):
        return None
    else:
        return json.loads(retData)
#[CODE 3]
def getPostData(post, jsonResult):   
   #이곳에 프로그램을 작성하세요
    title=post['title']
    description=post['description']
    org_link=post['originallink']
    link=post['link']
                                                      #Thu, 18 Jan 2018 11:31:00 +0900
    pDate=datetime.datetime.strptime(post['pubDate'],'%a, %d %b %Y %H:%M:%S +0900')
    pDate=pDate.strftime('%Y-%m-%d%H:%M:%S')
    jsonResult.append({'title':title,
                       'description':description,
                       'org_link':org_link,
                       'link':org_link,
                       'pDate':pDate})
    return



def main():
   #이곳에 프로그램을 작성하세요
    jsonResult=[]
    sNode='news'
    search_text='비트코인'
    display_count=100
    jsonSearch=getNaverSearchResult(sNode,search_text,1,display_count)
    while((jsonSearch!=None)and (jsonSearch['display']!=0)):
        for post in jsonSearch['items']:
            getPostData(post,jsonResult)
        nStart=jsonSearch['start']+jsonSearch['display']
        jsonSearch=getNaverSearchResult(sNode,search_text,nStart,display_count)

    with open('%s_naver_%s.json'%(search_text,sNode),'w',encoding='utf-8')as outfile:
        retJson=json.dumps(jsonResult,
                           indent=4, sort_keys=True,
                           ensure_ascii=False)
        outfile.write(retJson)
    print("%s_naver_%s.json SAVED"%(search_text, sNode))
    

    
if __name__ == '__main__':
    main()
