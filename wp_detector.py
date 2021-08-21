from sys import version
import requests
import re
#  this function was detected wp web site
def wp_find(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = str(response.content)
            re_path_wp = re.compile(r'wp-[/\w+/g]')
            re_path_version = re.compile(r'WordPress [0-9]?[0-9].[0-9]?[0-9]')
            result = re.search(re_path_version,data)
            if result:
                return {"wp":True,"version":result.group()}
            elif re.search(re_path_wp,data):
                return {"wp":True,"version":"cant detect"}
            else:
                return {"wp":False,"version":None}
                
        else:
            return{"err":f"your response code was {response.status_code}"}
    except:
        return{"err":"we cant find your web site"}
        
# this function was check url pattern 
def url_check(url):
    re_path=r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
    if bool(re.match(re_path,url)):
        return wp_find(url)
    else:
        return{"err":"your url was not correct please sure you have been use http or https on first of your url"}
