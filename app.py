import requests
import re
def wp_find(url):
    try:
        respinse = requests.get(url)
        if respinse.status_code == 200:
            data = str(respinse.content)
            re_path = re.compile(r'wp-[/\w+/g]')
            resualt = re.search(re_path,data)
            if resualt:
                print("this is wp ")
            else:
                print("it's not wp")
        else:
            print(f"your response code was {respinse.status_code}")
    except:
        print("we cant find your web site")
def url_check(url):
    re_path=r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
    if bool(re.match(re_path,url)):

    # if bool(re.match(re_path,url)):
        wp_find(url)
    else:
        print("your url was not coreect plese sure you have been use http or https on first of your url")
def help():
    print("""
          this program will help you to find wordpress web site 
          
          
          your url is : <your target website url>
          
          if you want to exit program just need use 'exit' 
          
          """)
def main():
    help()
    while True:
        inp = input("your url is : ")
        if inp != "exit":
            url_check(inp)
        else:
            break
if __name__ == "__main__":
    main()
