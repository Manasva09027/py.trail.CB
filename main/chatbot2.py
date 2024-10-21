import requests
from bs4 import BeautifulSoup
# import ChatBot


def inp():
    
     qq=input('user>>>')
     URL ="https://www.google.co.in/search?q="+qq
     headers={
         'UA':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
     }
     page=requests.get(URL, headers=headers)
     soup= BeautifulSoup(page.content, 'html.parser')
     result=soup.find(class_='Z0LcW t2b5Cf CfV8xf').get_text()
     print(result)   
     
while True :
    inp()
    qc=input('To continue presss y: ')
    if qc!='y':
        break
    
        