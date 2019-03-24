import sys
import urllib.request
import json
if __name__ == '__main__':
    page_name="sejongbamboo"
    app_id="174720823286694"
    app_secret="88c7a1323cbe3ebb2d470c24c0d75cab"
    access_token=app_id+"|"+app_secret
    base="http://graph.facebook.com/v2.11"
    node="/"+page_name
    parameters="/?access_token=%s"%access_token
    url=base+node+parameters
    req=urllib.request.Request(url)
    try:
        response=urllib.request.urlopen(req)
        if response.getcode()==200:
            data=json.loads(response.read().decode('utf-8'))
            page_id=data['id']
            print("%s Facebook Numeric ID : %s"%(page_name,page_id))

    except Exception as e:
        print(e)
