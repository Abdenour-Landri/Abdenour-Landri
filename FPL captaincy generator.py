import random

list_of_captain =[]
while True:
    try:
        number= int(input("how many captaincy pick you\'re gonna enter? "))
        break
    except:
        print("enter a valid number(1,2,5,10)")
        continue




def add():
    i=0
    while i<number:
        add = input("enter a captaincy pick: ").capitalize()
        list_of_captain.append(add)
        i = i+1
    return list_of_captain

def who_your_captain():
    print()
    print("you\'re choices were: ")
    for x ,cap in enumerate(list_of_captain,start=1):
        print(x,"-",cap)
    
    captain= random.randrange(0, number, 1)
    print()
    print("you're captain is:",list_of_captain[captain])

add()
who_your_captain()
