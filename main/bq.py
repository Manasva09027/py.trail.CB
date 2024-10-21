
import bq 
import subprocess


def quiz():

# all questions
    que1="which is the largest land animal in the world."
    que2="largest continent on earth."
    que3="what is capital of france."

 #all answers
    aue1="elephant"
    aue2="asia"
    aue3="paris"


#introduction


#que1
    print("Question 1- ",que1)
    ans1=str(input("Answer:" ))
    if ans1 == aue1:
        print("answer is correct ")
    else:
        print("WRONG ANSWER !!!!!") 



#que2
    print("Question 2- ",que2)
    ans2=str(input("Answer:" ))
    if ans2 == aue2:
        print("answer is correct ")
    else:
        print("WRONG ANSWER !!!!!") 



#que3
    print("Question 3- ",que3)
    ans3=str(input("Answer:" ))
    if ans3 == aue3:
        print("answer is correct ")
    else:
        print("WRONG ANSWER !!!!!") 

#results
    if ans1+ans2+ans3 == aue1+aue2+aue3 :
            print("\n              CONGRATULATION   YOU   WON   THE   QUIZ   !! !! !!" )
    else:
                print("!!!!!!!!!!!!!!!!!!  YOU    LOSE  !!!!!!!!!!!!!!!!!!")
            

    

            

