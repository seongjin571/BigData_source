import sys
import urllib.request
import json

if __name__=='__main__':
    page_name="sejongbamboo"
    page_id="479819552144174"
    app_id="174720823286694"
    app_secret="88c7a1323cbe3ebb2d470c24c0d75cab"

    from_date="2017-12-01"
    to_date="2017-12-31"
    num_statuses="10"
    access_token=app_id+"|"+app_secret

    base="http://graph.facebook.com/v2.11"
    node="/%s/posts"%page_id
    fields="/?fields=id,message,link,name,type,shares,reactions,"+\
            "created_time,comments.limit(0).summary(true)"+\
            ".limit(0).summary(true)"
    duration="&since=%s&until=%s"%(from_date,to_date)
    parameters="&limit=%s&access_token=%s"%(num_statuses,access_token)
    url=base+node+fields+duration+parameters

    req=urllib.request.Request(url)
    try:
        response=urllib.request.urlopen(req)
        if response.getcode()==200:
            data=json.loads(response.read().decode('utf-8'))
            print(data)
    except Exception as e:
        print(e)
