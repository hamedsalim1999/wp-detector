from setup import wp_check
import requests
def main(url):
    try:
        resualt = requests.get(url).status_code
        if resualt == 200:
            print(wp_check(url))
        else:
            print(resualt)
    except:
        print("error")

if __name__ == '__main__':
	main("https://www.digikala.com/")