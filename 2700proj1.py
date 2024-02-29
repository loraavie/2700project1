"""
Use: for giving the answer to yes or no questions
"""
def y_or_n(inp):

    if(inp.upper()=="YES" or inp.upper()=="Y"):
        ans = True
        return 5
    elif(inp.upper()=="NO" or inp.upper()=="N"):
        ans = False
        return 0
    else:
        inp = input("Invalid Input: try again")
        y_or_n(inp)

"""
Use: for giving the answer to how much questions 
ex: 'how often do you do this' 'how much does this apply to you'
ideal input is a scale 1-5
"""
def how_much(inp):
    while True:
        try:
            return int(inp)
        except:
            input("Your input was not a number. Try again.")

"""Loops until an input number is reached. If quiz has 5 questions
inp = 5. Can either be modified to have questions directly inside each case or """
def game_loop(inp):

    res1 = 0
    res2 = 0
    res3 = 0
    x = 0
    while x<inp:
        match x:
            case 0:
                print("question 1")
                inp= how_much(input())
                res1= res1+inp
                print(inp)


            case 1:
                print("question 2")
            case 2:
                print("question 3")
            case 3:
                print("question 4")
            case 4:
                print("question 5")
        x=x+1
    if res1>=res2 and res1>=res3:
        ending1()
    elif res2>=res1 and res2>=res3:
        ending2()
    elif res3>=res1 and res3>=res2:
        ending3()

def ending1():
    print("This is ending one. This means...")
def ending2():
    print("This is ending two. This means...")
def ending3():
    print("This is ending three. This means...")
game_loop(4)
