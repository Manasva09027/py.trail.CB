# IMPORTING
from googlesearch import search
import subprocess
import sys
import os
import time


     #CHATBOT CODES
#Questi
q1="who are you"
q2="who made you"
q3="what you can do"
q4="tell me a joke"
q5="ask me a quiz"
q6="tell me about you"
q7="what is your name"
q8="hello"
q9="how are you"
q10="recomend me some songs"
q11="yo"
  
  #Answers
a1="I am a alex a python chatbot."
a2="I was created by Manasva by coding."
a3="I can solve any mathemetical problem or you can ask some questions to me according to my data."
a4="\n Laptop- I cant remove this cap from me \n pc- because your CapsLock is on yo. \n \t hahaha....."
a6="I am Alex, a python chatbot , am capable of solving mathametival problems and to answer some questions according to my data."
a7="Hi my name is Alex , How can I assit you. "
a8="Hello user, nice to meet you ."
a9="I am fine thank you user and how about you ."
a10="\n Here you can try some of this:\n \n despasito \t\t by- louis fonsi \n levitating\t\t by- dua lipa \n no lie \t\t by- san paul & dua lipa \n dream on\t\t by- aerosmith \n way down we go\t\t by- kaleo \n unstopable\t\t by- sia \n world smallest violin\t\t by- AJR"
a11="yo what's up buddy \n how can i assist you today."
#FUNCTION

w=input("type>>>>> ")

if w==q1:
    print(a1)
elif w== q2:
   print(a2)
elif w== q3:
    print(a3)
elif w== q4:
    print(a4)
elif w=="hey":
    print(a7)
elif w=="yo":
    print(a7)
elif w=="hi":
    print(a7)
# elif w== q5:
#     subprocess.run(["python","bq.py"])
elif w== q6:
    print(a6)
elif w== q7:
   print(a7)
elif w== q8:
    print(a8)
elif w== q9:
    print(a9)
elif w== q10:
    print(a10)
elif w== q11:
    print(a11)
elif w=='stop':
     exit
else:
    for i in search (w, tld="com", num=6, stop=6,):
        print("Here are some results by google: \n \t \t",i ,'\n')
 
time.sleep(3)
subprocess.call([sys.executable, os.path.realpath(__file__)]+sys.argv[1:])

