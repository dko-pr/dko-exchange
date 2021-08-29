import requests

if __name__ == '__main__':
    #url = r"https://customers.rai.ir"
    url = r"http://www.transinform.info"
    session = requests.Session()
    content = session.get(url)
    print(content)
