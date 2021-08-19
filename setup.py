import urllib.request
import requests

def wp_check(url):
    header = "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'"
    url_wpl = url + "/wp-login.php"
    url_wpac = url + "/wp-content/"
    url_wpad = url + "/wp-admin/"
    url_wpc = url + "/wp-cron.php"
    url_wpx = url + "/xmlrpc.php"
    url_wpa = url + "/wp-json/wp/v2/"
    url_wpact = url + "/wp-content/themes/"

    req_wpl = urllib.request.Request(url_wpl, headers={'User-Agent': header})
    req_wpac = urllib.request.Request(url_wpac, headers={'User-Agent': header})
    req_wpact = urllib.request.Request(url_wpact, headers={'User-Agent': header})
    req_wpacp = urllib.request.Request(url_wpact, headers={'User-Agent': header})
    req_wpad = urllib.request.Request(url_wpad, headers={'User-Agent': header})
    req_wpc = urllib.request.Request(url_wpc, headers={'User-Agent': header})
    req_wpx = urllib.request.Request(url_wpx, headers={'User-Agent': header})
    req_wpa = urllib.request.Request(url_wpa, headers={'User-Agent': header})

    try:
        if urllib.request.urlopen(req_wpa):
            return True
            
    except urllib.error.HTTPError:
        try:
            if urllib.request.urlopen(req_wpl):
                return True
                
        except urllib.error.HTTPError:
            try:
                if urllib.request.urlopen(req_wpac):
                    return True
                    
            except urllib.error.HTTPError:
                try:
                    if urllib.request.urlopen(req_wpact):
                        return True
                        
                except urllib.error.HTTPError:
                    try:
                        if urllib.request.urlopen(req_wpacp):
                            return True
                            
                    except urllib.error.HTTPError:
                        try:
                            if urllib.request.urlopen(req_wpad):
                                return True
                                
                        except urllib.error.HTTPError:
                            try:
                                if urllib.request.urlopen(req_wpc):
                                    return True
                                    
                            except urllib.error.HTTPError:
                                try:
                                    if urllib.request.urlopen(req_wpx):
                                        return True
                                        
                                except urllib.error.HTTPError:
                                    
                                    return False


